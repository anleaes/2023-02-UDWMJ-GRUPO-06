from django.db import models
from django.db import models
from treino.models import Treino

# Create your models here.
class Profissional(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    profissional_treino = models.ManyToManyField(Treino, through='ProfissionalTreino', blank=True)
    
    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissional'
        ordering =['id']

    def __str__(self):
        return self.first_name
    
class ProfissionalTreino(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    Profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Plano alimentar'
        verbose_name_plural = 'Itens de Plano alimentar'
        ordering =['id']

    def __str__(self):
        return self.treino.name
