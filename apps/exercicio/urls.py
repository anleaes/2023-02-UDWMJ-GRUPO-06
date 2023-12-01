from django.urls import path
from . import views

app_name = 'exercicio'

urlpatterns = [
    path('', views.list_exercicio, name='list_exercicio'),
    path('adicionar/<int:id_profissional>/', views.add_exercicio_item, name='add_exercicio'),
    path('excluir/<int:id_exercicio>/', views.delete_exercicio, name='delete_exercicio'),
    path('excluir-item/<int:id_exercicio_item>/', views.delete_exercicio_item, name='delete_exercicio_item'),
    path('adicionar-item/<int:id_exercicio>/', views.add_exercicio_item, name='add_exercicio_item'),
    path('editar-status/<int:id_exercicio>/', views.edit_exercicio_status, name='edit_exercicio_status'),
]
