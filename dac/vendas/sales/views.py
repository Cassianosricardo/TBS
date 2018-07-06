from django.shortcuts import render
import requests

# Create your views here.

def listReports(request):
    return render(request,'reports.html')
    
def sales(request):
    products = requests.get('http://172.19.0.4:8000/list').json()        
    return render(request,'sales.html',{'products':products})

# vendas → view_vendas → request update api → processa → redireciona 