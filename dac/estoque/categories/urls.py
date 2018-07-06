from django.urls import path
from .views import list_categories, create_categorie, update_categorie, delete_categorie, listall, listOne, listProducts

urlpatterns = [
    path('', list_categories, name='list_categories'),
    path('new', create_categorie, name='create_categorie'),
    path('update/<int:id>/', update_categorie, name='update_categorie'),
    path('delete/<int:id>/', delete_categorie, name='delete_categorie'),
    path('list/', listall , name='list all'),
    path('list/<int:id>', listOne, name='list One'),
    path('get/<int:id>', listProducts, name='listProducts'),

]


# CRUD - CREATE, READ, UPDATE, DELETE