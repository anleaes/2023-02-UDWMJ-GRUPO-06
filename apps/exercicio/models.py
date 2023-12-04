from django.db import models
from treino.models import Treino
from profissional.models import Profissional

# Create your models here.

class Exercicio(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    exercicio_item = models.ManyToManyField(Treino, through='ExercicioItem', blank=True)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 


class ExercicioItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Exercicio'
        verbose_name_plural = 'Itens de Exercicio'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity)