from django.db import  models
from .product import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    productid = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_cart_by_customer(customer_id):
        return Cart.objects.filter(customer = customer_id)
    

    

    
