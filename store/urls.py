from django.urls import path
from store import views




urlpatterns=[
path('',views.home,name='home'),


path('home',views.home,name='home'),


path('products',views.all_product,name ='Product'),


path('contact',views.contact,name='contact'),


path('faq',views.faq,name='faq'),


path('favorites',views.favorites,name='favorites'),


path('basket',views.basket,name='basket'),


path('sign_up',views.sign_up,name='sign_up'),


path('sign_in',views.sign_in,name='sign_in'),


path('checkout',views.checkout,name='checkout'),


]