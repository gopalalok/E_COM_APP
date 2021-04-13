from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from django.contrib.auth.models import User
from django.views import  View
from store.models.product import Product



class Cart(View):
    def get(self , request):
        products = {}
        if request.session.get('cart'):
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
        return render(request , 'cart.html',{'products':products})
        

    