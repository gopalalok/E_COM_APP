from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.product import Product
from store.models.cart import Cart
from django.views import  View


def logout(request):
    customer = request.user
    cart = request.session.get('cart')

    if(cart):
        for key,values in cart.items():
            savecart = Cart(customer = customer,
                        productid = key,
                        quantity = values)
            savecart.save()

    request.session.clear()
    return redirect('login')

def error_404_view(request, exception):
    data = {"name": "http://127.0.0.1:8000/"}
    return render(request,'error_404.html', data)
    
    
