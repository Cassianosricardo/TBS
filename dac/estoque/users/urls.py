from django.urls import path
from .views import list_users, update_user, delete_user
from . import views

urlpatterns = [
    path('', list_users, name='list_users'),
    path('signup/', views.SignUp.as_view(), name='signup'),    
    path('update/<int:id>/', update_user, name='update_user'),
    path('delete/<int:id>/', delete_user, name='delete_user'),
]