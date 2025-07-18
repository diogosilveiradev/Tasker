from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto
from .forms import ProjetoForm

@login_required
def lista_projetos(request):
    projetos = Projeto.objects.filter(dono=request.user)
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

@login_required
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.dono = request.user
            projeto.save()
            return redirect('projetos:lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/form_projeto.html', {'form': form, 'titulo': 'Criar Projeto'})

@login_required
def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk, dono=request.user)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos:lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projetos/form_projeto.html', {'form': form, 'titulo': 'Editar Projeto'})

@login_required
def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk, dono=request.user)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos:lista_projetos')
    return render(request, 'projetos/confirma_exclusao.html', {'projeto': projeto})
