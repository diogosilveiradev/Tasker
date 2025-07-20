from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from projetos.models import Projeto
from .forms import TarefaForm

@login_required
def lista_tarefas(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id, dono=request.user)
    tarefas = projeto.tarefas.all()
    return render(request, 'tarefas/lista_tarefas.html', {'projeto': projeto, 'tarefas': tarefas})

@login_required
def criar_tarefa(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.projeto = projeto
            tarefa.save()
            return redirect('tarefas:lista_tarefas', projeto_id=projeto.id)
    else:
        form = TarefaForm()

    return render(request, 'tarefas/form_tarefa.html', {
        'form': form,
        'projeto': projeto
    })


@login_required
def editar_tarefa(request, projeto_id, tarefa_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, projeto=projeto)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista_tarefas', projeto_id=projeto.id)
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'projeto': projeto})


@login_required
def excluir_tarefa(request, projeto_id, tarefa_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, dono=request.user)
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, projeto=projeto)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas:lista_tarefas', projeto_id=projeto.id)
    return render(request, 'tarefas/confirma_exclusao.html', {'tarefa': tarefa, 'projeto': projeto})

@login_required
def detalhar_tarefa(request, projeto_id, tarefa_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, dono=request.user)
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, projeto=projeto)
    return render(request, 'tarefas/detalhar_tarefa.html', {'projeto': projeto, 'tarefa': tarefa})
