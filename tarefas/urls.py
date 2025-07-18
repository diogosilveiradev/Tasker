from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('projeto/<int:projeto_id>/', views.lista_tarefas, name='lista_tarefas'),
    path('projeto/<int:projeto_id>/criar/', views.criar_tarefa, name='criar_tarefa'),
    path('projeto/<int:projeto_id>/editar/<int:pk>/', views.editar_tarefa, name='editar_tarefa'),
    path('projeto/<int:projeto_id>/excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
]
