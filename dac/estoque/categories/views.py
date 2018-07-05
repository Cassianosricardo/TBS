from django.shortcuts import render, redirect
from .models import Categorie
from .forms import CategorieForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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
