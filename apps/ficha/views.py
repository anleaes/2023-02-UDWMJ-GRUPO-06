from django.shortcuts import render, get_object_or_404, redirect
from .forms import FichaForm
from .models import Ficha
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/contas/login/')
def add_ficha(request):
    template_name = 'ficha/add_ficha.html'
    context = {}
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('ficha:list_ficha')
    form = FichaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_ficha(request):
    template_name = 'ficha/list_ficha.html'
    ficha = Ficha.objects.filter()
    #fichas = Ficha.objects.filter() possivel erro
    context = {
        'ficha': ficha
    }
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def edit_ficha(request, id_ficha):
    template_name = 'ficha/add_ficha.html'
    context ={}
    ficha = get_object_or_404(Ficha, id=id_ficha)
    #fichas
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('ficha:list_ficha')
    form = FichaForm(instance=ficha)
    context['form'] = form
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def delete_ficha(request, id_ficha):
    ficha = Ficha.objects.get(id=id_ficha)
    #fichas
    ficha.delete()
    return redirect('ficha:list_ficha')