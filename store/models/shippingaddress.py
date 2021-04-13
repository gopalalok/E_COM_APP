from django.db import  models
from .product import Product
from .orderidmerge import Orderidmerge

class Shippingaddress(models.Model):
    order = models.ForeignKey(Orderidmerge, on_delete = models.CASCADE)
    fullname = models.CharField(max_length=100, default='', blank=True)
    mobilenumber = models.CharField(max_length=50, default='', blank=True)
    pincode = models.CharField(max_length=20, default='', blank=True)
    flat = models.CharField(max_length=50, default='', blank=True)
    area = models.CharField(max_length=100, default='', blank=True)
    landmark = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=50, default='', blank=True)

    

    


