from django import forms
from .models import Palimentar

class PalimentarForm(forms.ModelForm):

    class Meta:
        model = Palimentar
        exclude = ('created_on' , 'updated_on',)