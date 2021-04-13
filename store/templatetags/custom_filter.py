from django import template
from store.models.subcategory import Subcategory
from store.models.orders import Order
import re 

register = template.Library()

@register.filter(name='currency')
def currency(number): 
    return "₹"+str(number)

@register.filter(name='multiply')
def multiply(number,price):  
    return number*price

@register.filter(name='fullname')
def fullname(fname,lname): 
    return fname+" "+lname

@register.filter(name='subcategory_filter')
def subcategory_filter(category_id):
    return Subcategory.get_all_subcategories_by_category_id(category_id)

@register.filter(name='listorderid_filter')
def listorderid_filter(order_id):
    l = re.findall(r'[0-9]+', order_id)
    return list(l)

@register.filter(name='orderid_filter')
def orderid_filter(order_id):
    return Order.get_orders_by_id(order_id)

