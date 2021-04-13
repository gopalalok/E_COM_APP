from django.shortcuts import render, redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.subcategory import Subcategory
from store.models.cart import Cart
from django.views import View
from django.core.paginator import Paginator

# Create your views here.
class Index(View):

    def post(self, request):
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
        return redirect('homepage')

    def get(self, request):
        customer = False
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        data = {}
        products = Product.get_all_products()
        data['categories'] = Category.get_all_categories()
        data['subcategories'] = Subcategory.get_all_subcategories()
        category_id = request.GET.get('category')
        if request.user.is_authenticated:
            customer = request.user
        savecart = Cart.get_cart_by_customer(customer)
        
        if savecart:
            for i in savecart:
                if str(i.productid) in cart:
                    cart[str(i.productid)] = cart[str(i.productid)] + i.quantity
                else:
                    cart[str(i.productid)] = i.quantity
            request.session['cart'] = cart
            savecart.delete()
        if category_id:
            data['products'] = Product.get_all_products_by_category_id(category_id)
        paginator = Paginator(products,12)
        page_number = request.GET.get('page')
        data['page_obj'] = paginator.get_page(page_number)    
        
        return render(request, 'index.html',data)