from django.shortcuts import render
from projetos.models import Projeto
from tarefas.models import Tarefa
from django.contrib.auth.models import User

def home(request):
    projetos = Projeto.objects.all()
    tarefas = Tarefa.objects.all()
    usuarios = User.objects.all()
    return render(request, 'home.html', {
        'projetos': projetos,
        'tarefas': tarefas,
        'usuarios': usuarios
    })
