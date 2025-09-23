from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحات العامة
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # عربة التسوق
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

    # نظام المستخدم
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
