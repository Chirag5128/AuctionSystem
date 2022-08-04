from tkinter import CASCADE
from django.db import models
from Products.models import Product
from Users.models import User

# Create your models here.

class Bid(models.Model):
    
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    bid_no = models.IntegerField(null=False)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    t_stamp = models.DateTimeField(auto_now = True)
    bid_amt = models.DecimalField(max_digits=10 ,decimal_places=2, null=False)
