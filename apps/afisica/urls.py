from django.urls import path
from . import views

app_name = 'afisica'

urlpatterns = [
    path('', views.list_afisica, name='list_afisica'),
    path('adicionar/', views.add_afisica, name='add_afisica'),
    path('editar/<int:id_afisica>/', views.edit_afisica, name='edit_afisica'),
    path('excluir/<int:id_afisica>/', views.delete_afisica, name='delete_afisica'),
]