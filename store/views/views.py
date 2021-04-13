from django.shortcuts import render, redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.core.paginator import Paginator


# Create your views here.

#def get(request):
    #paginator = Paginator(products,4)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #data = {'products':products,'query':query,'page_obj':page_obj}
    #return render(request, 'search.html',data)