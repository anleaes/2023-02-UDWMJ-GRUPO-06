from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlimentoForm, AlimentoItemForm
from .models import Alimento , AlimentoItem, Palimentar, Client

# Create your views here.

def add_alimento(request, id_client):
    template_name = 'alimento/add_alimento.html'
    context = {}
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Client.objects.get(id=id_client)
            f.save()
            form.save_m2m()
            return redirect('alimento:list_alimento')
    form = AlimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_alimento(request):
    template_name = 'alimento/list_alimento.html'
    alimento = Alimento.objects.filter()
    alimento_items = AlimentoItem.objects.filter()
    palimentar = Palimentar.objects.filter()
    clients = Client.objects.filter()
    context = {
        'alimento': alimento,
        'alimento_items': alimento_items,
        'palimentar': palimentar,
        'clients': clients
    }
    return render(request, template_name, context)

def delete_alimento(request, id_alimento):
    alimento = Alimento.objects.get(id=id_alimento)
    alimento.delete()
    return redirect('alimento:list_alimento')

def add_alimento_item(request, id_alimento):
    template_name = 'alimento/add_alimento_item.html'
    context = {}
    if request.method == 'POST':
        form = AlimentoItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.alimento = Alimento.objects.get(id=id_alimento)
            f.save()
            form.save_m2m()
            return redirect('alimento:list_alimento')
    form = AlimentoItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_alimento_item(request, id_alimento_item):
    alimentoitem = AlimentoItem.objects.get(id=id_alimento_item)
    alimentoitem.delete()
    return redirect('alimento:list_alimento')

def edit_alimento_status(request, id_alimento):
    template_name = 'alimento/edit_alimento_status.html'
    context ={}
    alimento = get_object_or_404(Alimento, id=id_alimento)
    if request.method == 'POST':
        form = AlimentoForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('alimento:list_alimento')
    form = AlimentoForm(instance=alimento)
    context['form'] = form
    return render(request, template_name, context)