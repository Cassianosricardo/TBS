# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@login_required
def list_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})

@staff_member_required
@login_required
def create_user(request):
    form = CustomUserCreationForm(request.POST or None)        
    if form.is_valid():        
        form.save()
        return redirect('list_users')

    return render(request, 'users-form.html', {'form': form})

@staff_member_required
@login_required
def update_user(request, id):
    user = CustomUser.objects.get(id=id)
    form = CustomUserCreationForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'signup.html', {'form': form, 'user': user})    

@staff_member_required(login_url='auth_error.html')
@login_required
def delete_user(request, id):
    user = CustomUser.objects.get(id=id)    
    if request.method == 'POST':        
        user.delete()        
        return redirect('list_users')
    return render(request, 'user-delete-confirm.html', {'user': user})


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = '/users/'
    template_name = 'signup.html'