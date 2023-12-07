from django import forms
from .models import Afisica

class AfisicaForm(forms.ModelForm):

    class Meta:
        model = Afisica
        exclude = ('created_on' , 'updated_on',)