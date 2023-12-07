from django.shortcuts import render, get_object_or_404, redirect
from .forms import AfisicaForm
from .models import Afisica

# Create your views here.

def add_afisica(request):
    template_name = 'afisica/add_afisica.html'
    context = {}
    if request.method == 'POST':
        form = AfisicaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('afisica:list_afisica')
    form = AfisicaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_afisica(request):
    template_name = 'afisica/list_afisica.html'
    afisica = Afisica.objects.filter()
    context = {
        'afisica': afisica,
    }
    return render(request, template_name, context)

def edit_afisica(request, id_afisica):
    template_name = 'afisica/add_afisica.html'
    context ={}
    afisica = get_object_or_404(Afisica, id=id_afisica)
    if request.method == 'POST':
        form = AfisicaForm(request.POST, instance=afisica)
        if form.is_valid():
            form.save()
            return redirect('afisica:list_afisica')
    form = AfisicaForm(instance=afisica)
    context['form'] = form
    return render(request, template_name, context)

def delete_afisica(request, id_afisica):
    afisica = Afisica.objects.get(id=id_afisica)
    afisica.delete()
    return redirect('afisica:list_afisica')
