from django import forms
from .models import Treino, Profissional, ExercicioItem ,Treino

class ExercicioForm(forms.ModelForm):
    
    class Meta:
        model = Treino
        exclude = ('profissional', 'created_on' , 'updated_on')

class ExercicioItemForm(forms.ModelForm):
    
    class Meta:
        model = ExercicioItem
        exclude = ('exercicio', 'created_on' , 'updated_on')