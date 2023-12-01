from django import forms
from .models import Alimento, Client, AlimentoItem ,Palimentar

class AlimentoForm(forms.ModelForm):
    
    class Meta:
        model = Alimento
        exclude = ('client', 'created_on' , 'updated_on')

class AlimentoItemForm(forms.ModelForm):
    
    class Meta:
        model = AlimentoItem
        exclude = ('alimento', 'created_on' , 'updated_on')