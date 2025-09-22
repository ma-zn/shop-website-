# catalog/views.py
from django.shortcuts import render
from .models import Category, Product
from datetime import datetime
from .models import Product
def home(request):
    context = {
        'year': datetime.now().year,
        'categories': Category.objects.all()[:8],
        'products': Product.objects.all()[:8],
    }
    return render(request, 'home.html', context)
def home(request):
    return render(request, 'home.html', {'year': datetime.now().year})

def products(request):
    return render(request, 'products.html', {'year': datetime.now().year})

def about(request):
    return render(request, 'about.html', {'year': datetime.now().year})

def contact(request):
    return render(request, 'contact.html', {'year': datetime.now().year})

def cart(request):
    return render(request, 'cart.html', {'year': datetime.now().year})
def products(request):
    return render(request, 'products.html', {
        'year': datetime.now().year,
        'products': Product.objects.all()
    })