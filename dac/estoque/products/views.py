from django.shortcuts import render, redirect
from .models import Product
from .serializers import ProductSerializer
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# @staff_member_required
@login_required(login_url='/users/login/')
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@staff_member_required
@login_required(login_url='/users/login/')
def create_product(request):
    form = ProductForm(request.POST or None)        
    if form.is_valid():        
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})

@staff_member_required
@login_required(login_url='/users/login/')
def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})

@login_required(login_url='/users/login/')
def receive_product(request, id):    
    product = Product.objects.get(id=id)        
    if request.POST:
        print(request.POST.get('qtd')) 
        if int(request.POST.get('qtd')) >= 0:
            product.quantity += int(request.POST.get('qtd'))
            product.save()
            return redirect('list_products')      
    return render(request, 'receive-product.html', {'product': product})

@staff_member_required
@login_required(login_url='/users/login/')
def delete_product(request, id):
    product = Product.objects.get(id=id)    
    if request.method == 'POST':        
        product.delete()        
        return redirect('list_products')
    return render(request, 'delete-product.html', {'product': product})

#### API METHODS ###

@csrf_exempt
@api_view(['GET'])
def listall(request):        
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def listOne(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)                
    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)

@csrf_exempt
@api_view(['POST'])
def update(request, id):    
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)                    
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 