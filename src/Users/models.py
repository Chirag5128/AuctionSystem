from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    psswd = models.CharField(max_length=80, null=False)
    phone = models.CharField(max_length=10)