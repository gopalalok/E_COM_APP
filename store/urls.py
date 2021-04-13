from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from .views.home import Index
from .view import SignUpView, ActivateAccount, profile, about
from .views.login import logout
from .views.cart import Cart
from .views.checkout import CheckOut, handlerequest
from .views.orders import OrderView

from .views.search import SearchView
from .views.view_product import ViewProduct
from .middlewares.auth import auth_middleware



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup/',SignUpView.as_view(), name = 'signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('login/',auth_middleware(auth_views.LoginView.as_view(template_name='login.html')), name = 'login'),
    path('logout', logout , name='logout'),
    path('cart/', Cart.as_view(), name = 'cart'),
    path('checkout', CheckOut.as_view(), name = 'checkout'),
    path('orders', OrderView.as_view(), name = 'orders'),
    path('profile/', profile, name = 'profile'),
    
    path('search/', SearchView.as_view(), name = 'search'),
    path('view_product/<int:id>', ViewProduct, name = 'view_product'),
    path('handlerequest/', handlerequest, name='HandleRequest'),
    path('about/', about, name='about'),
]

