from django.urls import path
from . import views
from tarefas import views as tarefas_views

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('novo/', views.criar_projeto, name='criar_projeto'),
    path('editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('excluir/<int:id>/', views.excluir_projeto, name='excluir_projeto'),
    path('detalhar/<int:id>/', views.detalhar_projeto, name='detalhar_projeto'),


    # Rotas de tarefas dentro de projetos
    path('<int:projeto_id>/tarefas/', tarefas_views.lista_tarefas, name='lista_tarefas'),
    path('<int:projeto_id>/tarefas/nova/', tarefas_views.criar_tarefa, name='criar_tarefa'),
    path('<int:projeto_id>/tarefas/<int:id>/editar/', tarefas_views.editar_tarefa, name='editar_tarefa'),
    path('<int:projeto_id>/tarefas/<int:id>/excluir/', tarefas_views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:projeto_id>/tarefas/<int:tarefa_id>/', tarefas_views.detalhar_tarefa, name='detalhar_tarefa'),
    

]
