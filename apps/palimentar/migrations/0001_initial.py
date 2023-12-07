# Generated by Django 4.1 on 2023-12-07 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palimentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(max_length=100, verbose_name='Descricao')),
                ('date_fabrication', models.DateField(verbose_name='Data Fabricacao')),
                ('is_active', models.BooleanField(default=False, verbose_name='Ativo')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Foto')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.ficha')),
            ],
            options={
                'verbose_name': 'palimentar',
                'verbose_name_plural': 'palimentar',
                'ordering': ['id'],
            },
        ),
    ]
