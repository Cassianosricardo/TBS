from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.

def listReports(request):
    return render(request,'reports.html')
    
def sales(request):
    if request.method == 'POST':
        print(request.data)
    products = requests.get('http://172.22.0.4:8000/list').json()        
    return render(request,'sales.html',{'products':products})

def getCategories(request):
    categories = requests.get('http://172.22.0.4:8000/categories/list/').json()    
    return JsonResponse(categories, safe=False)

def getProducts(request, id):
    categories = requests.get('http://172.22.0.4:8000/categories/get/'+ str(id)).json()    
    return JsonResponse(categories, safe=False)

def getProduct(request, id):
    categories = requests.get('http://172.22.0.4:8000/get/'+ str(id)).json()    
    return JsonResponse(categories, safe=False)

@csrf_exempt
def finish(request):
    print (request.POST)
    response = requests.post('http://172.22.0.4:8000/mass_update/')    
    # categories = requests.get('http://172.22.0.4:8000/get/'+ str(id)).json()    
    return JsonResponse(request.post.data(), safe=False)



# vendas → view_vendas → request update api → processa → redireciona 