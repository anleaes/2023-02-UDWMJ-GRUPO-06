from django.urls import path
from . import views

app_name = 'palimentar'

urlpatterns = [
    path('', views.list_palimentar, name='list_palimentar'),
    path('adicionar/', views.add_palimentar, name='add_palimentar'),
    path('editar/<int:id_palimentar>/', views.edit_palimentar, name='edit_palimentar'),
    path('excluir/<int:id_palimentar>/', views.delete_palimentar, name='delete_palimentar'),
]