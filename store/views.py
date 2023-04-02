from django.shortcuts import render
from django.http import HttpResponse
from store.models import Category,Product





def categories(request):
    return {
        'categories': Category.objects.all()
    }



def home(request):
    return render(request,'store/home.html')

def all_product(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def contact(request):
    return render(request,'store/contact.html')

def faq(request):
    return render(request,'store/faq.html')

def favorites(request):
    return render(request,'store/favorites.html')

def basket(request):
    return render(request, 'store/basket.html')

def sign_up(request):
    return render(request, 'store/sign_up.html')

def sign_in(request):
    return render(request, 'store/sign_in.html')

def checkout(request):
    return render(request,'store/checkout.html')