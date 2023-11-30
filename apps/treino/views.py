from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TreinoForm
from .models import Treino
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/contas/login/')
def add_treino(request):
    template_name = 'treino/add_treino.html'
    context = {}
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('treino:list_treino')
    form = TreinoForm()
    context['form'] = form
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def list_treino(request):
    template_name = 'treino/list_treino.html'
    treino = Treino.objects.filter()
    context = {
        'treino': treino
    }
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def edit_treino(request, id_treino):
    template_name = 'treino/add_treino.html'
    context ={}
    treino = get_object_or_404(treino, id=id_treino)
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES,  instance=treino)
        if form.is_valid():
            form.save()
            return redirect('treino:list_treino')
    form = TreinoForm(instance=treino)
    context['form'] = form
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def delete_treino(request, id_treino):
    treino = Treino.objects.get(id=id_treino)
    treino.delete()
    return redirect('treino:list_treino')