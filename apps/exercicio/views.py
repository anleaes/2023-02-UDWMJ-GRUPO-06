from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExercicioForm, ExercicioItemForm
from .models import Exercicio , ExercicioItem, Treino, Profissional

# Create your views here.

def add_exercicio(request, id_client):
    template_name = 'exercicio/add_exercicio.html'
    context = {}
    if request.method == 'POST':
        form = ExercicioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Profissional.objects.get(id=id_client)
            f.save()
            form.save_m2m()
            return redirect('exercicio:list_exercicio')
    form = ExercicioForm()
    context['form'] = form
    return render(request, template_name, context)

def list_exercicio(request):
    template_name = 'exercicio/list_exercicio.html'
    exercicio = Exercicio.objects.filter()
    exercicio_items = ExercicioItem.objects.filter()
    treino = Treino.objects.filter()
    profissional = Profissional.objects.filter()
    context = {
        'exercicio': exercicio,
        'exercicio_items': exercicio_items,
        'treinos': treino,
        'profissional': profissional
    }
    return render(request, template_name, context)

def delete_exercicio(request, id_exercicio):
    exercicio = Exercicio.objects.get(id=id_exercicio)
    exercicio.delete()
    return redirect('exercicio:list_exercicio')

def add_exercicio_item(request, id_exercicio):
    template_name = 'exercicio/add_exercicio_item.html'
    context = {}
    if request.method == 'POST':
        form = ExercicioItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.exercicio = Exercicio.objects.get(id=id_exercicio)
            f.save()
            form.save_m2m()
            return redirect('exercicio:list_exercicio')
    form = ExercicioItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_exercicio_item(request, id_exercicio_item):
    exercicioitem = ExercicioItem.objects.get(id=id_exercicio_item)
    exercicioitem.delete()
    return redirect('exercicio:list_exercicio')

def edit_exercicio_status(request, id_exercicio):
    template_name = 'exercicio/edit_exercicio_status.html'
    context ={}
    exercicio = get_object_or_404(Exercicio, id=id_exercicio)
    if request.method == 'POST':
        form = ExercicioForm(request.POST, instance=exercicio)
        if form.is_valid():
            form.save()
            return redirect('exercicio:list_exercicio')
    form = ExercicioForm(instance=exercicio)
    context['form'] = form
    return render(request, template_name, context)
