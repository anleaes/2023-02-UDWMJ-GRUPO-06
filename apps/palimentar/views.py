from django.shortcuts import render, get_object_or_404, redirect
from .forms import PalimentarForm
from .models import Palimentar
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/contas/login/')
def add_palimentar(request):
    template_name = 'palimentar/add_palimentar.html'
    context = {}
    if request.method == 'POST':
        form = PalimentarForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('palimentar:list_palimentar')
    form = PalimentarForm()
    context['form'] = form
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def list_palimentar(request):
    template_name = 'palimentar/list_palimentar.html'
    palimentar = Palimentar.objects.filter()
    context = {
        'palimentar': palimentar
    }
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def edit_palimentar(request, id_palimentar):
    template_name = 'palimentar/add_palimentar.html'
    context ={}
    palimentar = get_object_or_404(Palimentar, id=id_palimentar)
    if request.method == 'POST':
        form = PalimentarForm(request.POST, request.FILES,  instance=palimentar)
        if form.is_valid():
            form.save()
            return redirect('palimentar:list_palimentar')
    form = PalimentarForm(instance=palimentar)
    context['form'] = form
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def delete_palimentar(request, id_palimentar):
    palimentar = Palimentar.objects.get(id=id_palimentar)
    palimentar.delete()
    return redirect('palimentar:list_palimentar')