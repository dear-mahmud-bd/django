from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE


# Create your models here.
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True) # initial null, if user does not put data then its okay
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, null=True, blank=False)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)