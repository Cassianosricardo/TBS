from django.contrib import admin
from django.urls import path, include
from .views import listReports, sales

urlpatterns = [
    path('', listReports, name="listReports"), 
    path('index', sales, name='sales'),
]