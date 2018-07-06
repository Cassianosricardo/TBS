from django.shortcuts import render
from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth

def list_products(request):    
    response = requests.get('http://172.22.0.4:8000/list')        
    data = response.json()    
    print (data)
    return render(request, 'products.html', {'data':data})    