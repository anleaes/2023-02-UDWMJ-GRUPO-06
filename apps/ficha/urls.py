from django.urls import path
from . import views

app_name = 'ficha'

urlpatterns = [
    path('', views.list_ficha, name='list_ficha'),
    path('adicionar/', views.add_ficha, name='add_ficha'),
    path('editar/<int:id_ficha>/', views.edit_ficha, name='edit_ficha'),
    path('excluir/<int:id_ficha>/', views.delete_ficha, name='delete_ficha'),
]