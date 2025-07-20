from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('<int:projeto_id>/', views.lista_tarefas, name='lista_tarefas'),
    path('<int:projeto_id>/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('<int:projeto_id>/<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:projeto_id>/<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:projeto_id>/<int:tarefa_id>/', views.detalhar_tarefa, name='detalhar_tarefa'),
]
