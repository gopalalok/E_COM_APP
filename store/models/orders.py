from django.db import  models
from .product import Product
from django.contrib.auth.models import User



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    
    
    
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)

    def get_orders_by_id(order_id):
        return Order.objects.get(pk=order_id)

    