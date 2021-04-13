from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.profile import Profile
from .models.orders import Order
from .models.profile import Profile
from .models.subcategory import Subcategory
from .models.cart import Cart
from .models.orderidmerge import Orderidmerge
from .models.shippingaddress import Shippingaddress

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','subcategory']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminSubcategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCart(admin.ModelAdmin):
    list_display = ['customer','productid','quantity']

class Adminorderidmerge(admin.ModelAdmin):
    list_display = ['customer','orderid','amount']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Cart,AdminCart)
admin.site.register(Subcategory,AdminSubcategory)
admin.site.register(Orderidmerge,Adminorderidmerge)
admin.site.register(Shippingaddress)