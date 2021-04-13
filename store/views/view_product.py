from django.shortcuts import render, redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.cart import Cart
from django.views import View
from django.urls import reverse


# Create your views here.
def ViewProduct(request,id):
    urlid = None
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(ViewProduct.urlid)
        return HttpResponseRedirect(reverse('view_product', args=[ViewProduct.urlid]))
    else:
        data = {}
        data['product'] = Product.objects.get(pk=id)
        ViewProduct.urlid = Product.objects.get(pk=id).id
        return render(request, 'view_product.html',data)