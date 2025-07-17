from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def lista_tarefas(request):
    return render(request, 'tarefas/lista.html')
