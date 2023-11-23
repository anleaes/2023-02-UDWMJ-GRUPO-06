from django import forms
from .models import Ficha

class FichaForm(forms.ModelForm):

    class Meta:
        model = Ficha
        exclude = ('created_on' , 'updated_on',)