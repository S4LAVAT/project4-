"""project_api URL Configuration

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
from gadgets.views import ProductList, ProductDetail, ProductDestroy, ProductCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', ProductList.as_view(), name='products'),
    path('products/<int:product_id>/delete', ProductDestroy.as_view(), name='products_destroy'),
    path('products/<int:product_id>', ProductDetail.as_view(), name='products_detail'),
    path('products/create', ProductCreate.as_view(), name='products_create')



]
