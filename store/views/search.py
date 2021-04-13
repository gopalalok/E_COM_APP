from django.shortcuts import render, redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.core.paginator import Paginator


# Create your views here.
class SearchView(View):
    search_products = None
    def post(self, request):
        pass

    def get(self, request):
        
        query = request.GET.get('query')
        if query:
            if len(query) > 50:
                products = Product.objects.none()
            else:
                allProductName = Product.objects.filter(name__icontains = query)
                allProductPrice = Product.objects.filter(price__icontains = query)
                SearchView.search_products = allProductName.union(allProductPrice)
        
        total_res = SearchView.search_products
        paginator = Paginator(SearchView.search_products,2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {'products':SearchView.search_products,'query':query,'page_obj':page_obj,'total_res':total_res}
        return render(request, 'search.html',data)