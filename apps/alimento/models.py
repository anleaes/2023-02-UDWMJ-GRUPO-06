from django.db import models
from palimentar.models import Palimentar
from clients.models import Client

# Create your models here.

class Alimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Alimento_item = models.ManyToManyField(Palimentar, through='AlimentoItem', blank=True)
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimento'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 


class AlimentoItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    palimentar = models.ForeignKey(Palimentar, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimento'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity)
