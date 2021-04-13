from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.models import User
from django.views import  View
from store.models.product import Product
from store.models.orders import Order
from store.models.orderidmerge import Orderidmerge
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class OrderView(View):
    def get(self , request):
        customer = request.user
        orders = Order.get_orders_by_customer(customer)
        orderidmerge = Orderidmerge.get_orderid_by_customer(customer)
        return render(request , 'orders.html',{'orders':orders,'orderidmerge':orderidmerge})

    