from django.urls import path
from . import views

app_name = 'treino'

urlpatterns = [
    path('', views.list_treino, name='list_treino'),
    path('adicionar/', views.add_treino, name='add_treino'),
    path('editar/<int:id_treino>/', views.edit_treino, name='edit_treino'),
    path('excluir/<int:id_treino>/', views.delete_treino, name='delete_treino'),
]

