from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from Users.models import User
from django.db import IntegrityError, transaction
from django.db.utils import DataError


# Create your views here.
def login_view(request):

    context = {}

    if request.method == "POST":
        uid = request.POST.get('uid')
        pswd = request.POST.get('psw')

        context = {'login' : 2}

        if User.objects.filter(user_id=uid[0]).exists():
            if User.objects.get(user_id = int(uid)).psswd == pswd:
                context["login"] = 1
                context['user_name'] = User.objects.get(user_id = int(uid)).name
                return HttpResponseRedirect('/userhome/')
            else:
                context['login'] = 0

        else:
            context['login'] = -1

    return HttpResponse(render(request,'user/login.html',context))

def register_view(request):

    context = {'uid_taken': -1}

    if request.method == "POST":
        user_name = request.POST.get("name")
        phone = request.POST.get("Phone Number")
        uid = request.POST.get("uid")
        email = request.POST.get("Email")
        password = request.POST.get("psw")

        try:
            with transaction.atomic():
                User.objects.create(name=user_name, phone=phone, user_id=uid, email=email, psswd=password)
                context['uid_taken'] = 0
                
                
        except (IntegrityError, DataError):
            context['uid_taken'] = 1




    return HttpResponse(render(request, 'user/register.html',context))

def user_home_view(request):
    context = {}
    return HttpResponse(render(request,'user/user.html', context))

def old_buy_view(request):
    context={}
    return HttpResponse(render(request,'user/oldbuy.html', context))

def old_sold_view(request):
    context = {}
    return HttpResponse(render(request, 'user/oldsell.html', context))