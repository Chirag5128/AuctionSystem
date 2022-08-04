from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest, HttpResponseRedirect
from .models import Product
from Bids.models import Bid
from Users.models import User
from django.db import IntegrityError, transaction
from django.db.utils import DataError
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model


# Create your views here.
def product_list_view(request):
    context = {}
    # obj = Product.objects.raw('select * from auctionsite.Products_Product where buyer_id_id is null')

    
    # prices = {}
    
    # for prod in obj:
    #     if Bid.objects.filter(prod_id_id=prod.prod_id).exists():
    #         price_dict = Bid.objects.filter(prod_id_id=prod.prod_id).aggregate(Max('bid_amt'))
    #         prices[prod.prod_id] = price_dict['bid_amt__max']
    #     else:
    #         prices[prod.prod_id] = prod.base_price

    # context = {'products':obj,
    #             'prices':prices,
    #             }
                
    return HttpResponse(render(request, 'product/product_list.html', context))

def add_product_view(request):
    context = {}
    print(request.POST)
    if request.method == 'POST':
        prod_name = request.POST.get('Product Name')
        prod_desc = request.POST.get('Description')
        base_p = request.POST.get('Starting Price')
        duration = request.POST.get('Duration')
        seller_id = request.POST.get('uid')
        pswd = request.POST.get('psw')
        image = request.POST.get('fileToUpload')

        try:
            with transaction.atomic():
                if User.objects.filter(user_id = seller_id).exists():
                    if User.objects.get(user_id = int(seller_id)).psswd == pswd:
                        Product.objects.create(name=prod_name, description=prod_desc, seller_id=User.objects.get(user_id = int(seller_id)), base_price=base_p, prod_img=image, duration=duration)
        
        except (IntegrityError, DataError):
            print("there was an error")


    
    return HttpResponse(render(request, 'product/sell.html', context))

import datetime
from datetime import timezone


def product_page_view(request, product_id):
    obj = Product.objects.get(prod_id=product_id)

    if Bid.objects.filter(prod_id=product_id).exists():
        
        
            prod_bids = Bid.objects.filter(prod_id=product_id)
            prod_price_dict = prod_bids.aggregate(Max('bid_amt'))
            prod_price = prod_price_dict['bid_amt__max']
    else:
        prod_price = obj.base_price

    end_date = obj.listing_date + datetime.timedelta(days=obj.duration)
    time_remaining = end_date - (datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=5, minutes=30))
    context = {'prod' : obj,
                'curr_price':prod_price,
                'time_left' : time_remaining,
                }

    if request.method == 'POST':
        bid_amount = request.POST.get('Enter your Bid Price')
        user_id = request.POST.get('uid')

        try:
            with transaction.atomic():
                if Bid.objects.filter(prod_id=product_id).exists():
                    #Bid.objects.get(prod_id=product_id)
                    prod_price_dict = Bid.objects.filter(prod_id=product_id).aggregate(Max('bid_amt'))
                    prod_price = prod_price_dict['bid_amt__max']
                else:
                    prod_price = obj.base_price

                if float(prod_price)>=float(bid_amount):
                    context['less_bid'] = True
                    return HttpResponse(render(request, 'product/productpage.html', context))
                else:
                    if Bid.objects.filter(prod_id=product_id).exists():
                        #Bid.objects.get(prod_id=product_id)
                        last_bid_no_dict = Bid.objects.filter(prod_id=product_id).aggregate(Max('bid_no'))
                        last_bid_no = last_bid_no_dict['bid_no__max']
                    else:
                        last_bid_no = 0

                    Bid.objects.create(bid_no=last_bid_no+1, bid_amt=bid_amount, prod_id_id=product_id, buyer_id_id=user_id)

            return HttpResponseRedirect('/userhome')
        
        except (IntegrityError, DataError):
            print("there was an error") 


    return HttpResponse(render(request, 'product/productpage.html', context))

