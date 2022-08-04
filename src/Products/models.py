from tkinter import CASCADE
from django.db import models
from Users.models import User
# Create your models here.

class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=300, null=True)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='+')
    base_price = models.DecimalField(max_digits=10 ,decimal_places=2, null=False)
    prod_img = models.ImageField(upload_to='images', null=True)
    listing_date = models.DateTimeField(auto_now = True)
    duration = models.IntegerField(default=5, null=False)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    buy_amt = models.DecimalField(max_digits=10 ,decimal_places=2, null=True)
    
