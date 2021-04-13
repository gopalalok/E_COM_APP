from django.shortcuts import render , redirect , HttpResponseRedirect
import uuid
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.models import User
from django.views import  View
from store.models.product import Product
from store.models.orders import Order
from store.models.cart import Cart
from store.models.orderidmerge import Orderidmerge
from store.models.shippingaddress import Shippingaddress
from django.views.decorators.csrf import csrf_exempt
from store.PayTm import Checksum
from django.http import HttpResponse
MERCHANT_KEY = '_%QEVAD#RNv8FjRa'
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class CheckOut(View):
   
    def get(self , request):
        return render(request , 'checkout.html')

    def post(self , request):
        payment = request.POST.get('payment')
        fullname = request.POST.get('fullname')
        mobilenumber = request.POST.get('mobilenumber')
        pincode = request.POST.get('pincode')
        flat = request.POST.get('flat')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')

        # validation
        values = {
            'payment':payment,
            'fullname': fullname,
            'mobilenumber': mobilenumber,
            'pincode': pincode,
            'flat': flat,
            'area':area,
            'landmark':landmark,
            'city':city,
            'state':state
        }
        error_message = None
        if(not payment):
            error_message = "Select Payment Options !!!"
        elif (not state):
            error_message = "Select State Required !!!"

        customer = request.user
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        customer_obj = customer
        order_id_list = []
        amount = 0
        transactionid = uuid.uuid1().hex
        if not error_message:
            for product in products:
                order = Order(customer = customer,
                                product = product,
                                price = product.price,
                                quantity = cart.get(str(product.id)))
                order.placeOrder()
                order_id_list.append(order.id)
                amount = amount + order.price * order.quantity
            if payment == "online": 
                orderidmerge = Orderidmerge(customer = customer,
                                    transactionid = transactionid,
                                    orderid = order_id_list,
                                    amount = amount,payment = "online")
            else:
                orderidmerge = Orderidmerge(customer = customer,
                                    transactionid = transactionid,
                                    orderid = order_id_list,
                                    amount = amount,payment = "cod")
            orderidmerge.save()
            
            shippingaddress = Shippingaddress(order = Orderidmerge(id = orderidmerge.id),
                            fullname=fullname,
                            mobilenumber=mobilenumber,
                            pincode=pincode,
                            flat=flat,
                            area = area,
                            landmark=landmark,
                            city = city,
                            state = state)
            shippingaddress.save()
            if payment == "online":
                
                param_dict={
                    'MID': 'LgWYcs58579287008550',
                    'ORDER_ID': str(orderidmerge.transactionid),
                    'TXN_AMOUNT': str(amount),
                    'CUST_ID': str(customer_obj.email),
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
                    }
                param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
                return  render(request, 'paytm.html', {'param_dict': param_dict})
            else:
                
                cart_obj = Cart.get_cart_by_customer(customer)
                cart_obj.delete()
                request.session['cart'] = {}
                response_dict = {
                    'RESPCODE' : "01",
                    'ORDERID' : orderidmerge.transactionid,
                }
                return render(request, 'paymentstatus.html', {'response': response_dict})
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request, 'checkout.html', data)

    

@csrf_exempt
def handlerequest(request):
    form = request.POST
    transactionid = request.POST.get('ORDERID')
    cust_email_id = request.POST.get('CUSTID')
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print(cust_email_id)
            customer = User.objects.get(email__exact=cust_email_id)
            cart_obj = Cart.get_cart_by_customer(customer)
            cart_obj.delete()
            request.session['cart'] = {}
            print('order successful')
        else:
            orderidmerge = Orderidmerge.get_orders_by_orderid(transactionid)
            orderidmerge.delete()
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})   