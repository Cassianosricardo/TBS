from django.contrib import admin
from django.urls import path, include
from .views import listReports, sales, getCategories, getProducts, getProduct, finish

urlpatterns = [
    path('', listReports, name="listReports"), 
    path('index', sales, name='sales'),
    path('categories', getCategories, name="Get Categories"), 
    path('products/<int:id>', getProducts, name="Get Products"), 
    path('product/<int:id>', getProduct, name="Get Product"), 
    path('finish/', finish, name="Finish"), 
]