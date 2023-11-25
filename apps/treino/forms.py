from django import forms
from .models import Treino

class TreinoForm(forms.ModelForm):

    class Meta:
        model = Treino
        exclude = ('created_on' , 'updated_on',)