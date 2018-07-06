from django.shortcuts import render, redirect
from .models import Categorie
from products.models import Product
from .forms import CategorieForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .serializers import CategorieSerializer
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

@staff_member_required
@login_required(login_url='/users/login/')
def list_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'categories.html', {'categories': categories})

@staff_member_required
@login_required(login_url='/users/login/')
def create_categorie(request):
    form = CategorieForm(request.POST or None)    
    print(request)
    if form.is_valid():        
        form.save()
        return redirect('list_categories')

    return render(request, 'categories-form.html', {'form': form})

@staff_member_required
@login_required(login_url='/users/login/')
def update_categorie(request, id):
    categorie = Categorie.objects.get(id=id)
    form = CategorieForm(request.POST or None, instance=categorie)

    if form.is_valid():
        form.save()
        return redirect('list_categories')

    return render(request, 'categories-form.html', {'form': form, 'categorie': categorie})

@staff_member_required
@login_required(login_url='/users/login/')
def delete_categorie(request, id):
    categorie = Categorie.objects.get(id=id)    
    if request.method == 'POST':        
        categorie.delete()        
        return redirect('list_categories')
    return render(request, 'delete-confirm.html', {'categorie': categorie})

## API METHODS

@api_view(['GET'])
@csrf_exempt
def listall(request):        
    categories = Categorie.objects.all()    
    serializer = CategorieSerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@csrf_exempt
def listOne(request, id):
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)                
    serializer = CategorieSerializer(categorie)
    return JsonResponse(serializer.data)

def listProducts(request, id):    
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)                    
    products = Product.objects.all()
    prodList = [x for x in products if x.categorie.id == id]
    serializer = ProductSerializer(prodList, many=True)    
    return JsonResponse(serializer.data, safe=False)