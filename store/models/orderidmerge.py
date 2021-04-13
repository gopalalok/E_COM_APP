from django.db import  models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Orderidmerge(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    transactionid = models.CharField(max_length= 500,default='')
    orderid = models.CharField(max_length= 500,default='')
    amount = models.IntegerField()
    payment = models.CharField(max_length= 50,default='')
    dtime = models.DateTimeField(default=datetime.datetime.now)

    def get_orders_by_orderid(transactionid):
        return Orderidmerge.objects.filter(transactionid = transactionid)

    def get_orderid_by_customer(customer_id):
        return Orderidmerge.objects.filter(customer = customer_id).order_by('-dtime')
