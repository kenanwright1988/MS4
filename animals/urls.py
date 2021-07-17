from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_animals, name='animals'),
    path('care/', views.all_animals_care, name='all_animals_care'),
    path('care/<int:animal_id>/', views.animal_care, name='animal_care'),
    path('<int:animal_id>/', views.animal_details, name='animal_details'),
    #  path('add/', views.add_product, name='add_product'),
    #  path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    #  path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
