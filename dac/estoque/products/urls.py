from django.urls import path
from .views import list_products, create_product, update_product, delete_product, receive_product, listall, listOne, update, mass_update

# CRUD - CREATE, READ, UPDATE, DELETE
urlpatterns = [

    path('', list_products, name='list_products'),
    path('new', create_product, name='create_product'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path('receive/<int:id>/', receive_product, name='receive_product'),
    path('list', listall, name='list'),
    path('api_update/<int:id>/', update, name='update'),
    path('get/<int:id>/', listOne, name='list_one'),
    path('mass_update/', mass_update, name='mass update'),
]
