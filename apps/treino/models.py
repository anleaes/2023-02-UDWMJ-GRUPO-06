from django.db import models
from ficha.models import Ficha

# Create your models here.
class Treino(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos')
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'treino'
        verbose_name_plural = 'treino'
        ordering =['id']

    def __str__(self):
        return self.name