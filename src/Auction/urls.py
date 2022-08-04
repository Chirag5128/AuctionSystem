"""Auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Pages.views import homepage
from Users.views import login_view, register_view, user_home_view, old_buy_view, old_sold_view
from Products.views import product_list_view, add_product_view, product_page_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('userhome/', user_home_view, name='user_home'),
    path('prodlist/', product_list_view, name='product_list'),
    path('sell/', add_product_view, name='add_product'),
    path('product_page/<int:product_id>/', product_page_view, name='product_page'),
    path('user_old_buy/', old_buy_view, name='old_buy'),
    path('user_old_sold/', old_sold_view, name='old_sold')
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 