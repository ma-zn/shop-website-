from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm  # النموذج المخصص للتسجيل

# -----------------------
# الصفحات العامة
# -----------------------
def home(request):
    categories = Category.objects.all()[:8]  # عرض أول 8 فئات
    products = Product.objects.all()[:8]     # عرض أول 8 منتجات
    return render(request, 'home.html', {
        'year': datetime.now().year,
        'categories': categories,
        'products': products
    })

def products(request):
    return render(request, 'products.html', {
        'year': datetime.now().year,
        'products': Product.objects.all()
    })

def about(request):
    return render(request, 'about.html', {'year': datetime.now().year})

def contact(request):
    return render(request, 'contact.html', {'year': datetime.now().year})

def cart(request):
    return render(request, 'cart.html', {'year': datetime.now().year})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {
        'product': product,
        'year': datetime.now().year
    })

# -----------------------
# نظام المستخدم
# -----------------------
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل دخول بعد إنشاء الحساب
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'year': datetime.now().year})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials',
                'year': datetime.now().year
            })
    return render(request, 'login.html', {'year': datetime.now().year})

def logout_view(request):
    logout(request)
    return redirect('home')

# -----------------------
# كارت التسوق
# -----------------------
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    cart[str(product.id)] = cart.get(str(product.id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')
