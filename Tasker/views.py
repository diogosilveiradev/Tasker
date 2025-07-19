from django.shortcuts import render
from projetos.models import Projeto, Tarefa
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    projetos = Projeto.objects.filter(dono=request.user)
    tarefas = Tarefa.objects.filter(projeto__dono=request.user, concluida=False)
    usuarios = User.objects.all() if request.user.is_superuser else None

    return render(request, 'home.html', {
        'projetos': projetos,
        'tarefas': tarefas,
        'usuarios': usuarios
    })
