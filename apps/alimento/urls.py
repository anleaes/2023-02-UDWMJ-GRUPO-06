from django.urls import path
from . import views

app_name = 'alimento'

urlpatterns = [
    path('', views.list_alimento, name='list_alimento'),
    path('adicionar/<int:id_client>/', views.add_alimento, name='add_alimento'),
    path('excluir/<int:id_alimento>/', views.delete_alimento, name='delete_alimento'),
    path('excluir-item/<int:id_alimento_item>/', views.delete_alimento_item, name='delete_alimento_item'),
    path('adicionar-item/<int:id_alimento>/', views.add_alimento_item, name='add_alimento_item'),
    path('editar-status/<int:id_alimento>/', views.edit_alimento_status, name='edit_alimento_status'),
]
