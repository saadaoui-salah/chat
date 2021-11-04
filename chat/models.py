from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

# class Usera(AbstractUser):
#     # id = models.AutoField(primary_key=True)
#     first_name = None
#     last_name = None
#     is_vendor = models.BooleanField(default=False)

# Create your models here.
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30) 
class Vender(models.Model):
    id = models.AutoField(primary_key=True)
    is_vendor = models.BooleanField(default=False)    
    user = models.OneToOneField(User , on_delete=models.CASCADE,  related_name='vender')

    def __str__(self):
        return f'{self.user}' 
    
class VendorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_profile')
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class CustomrProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    
class MemberProfile(models.Model):
    vandor_profile = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254, blank=True, verbose_name='email address')
     
    def __str__(self):
        return self.name
