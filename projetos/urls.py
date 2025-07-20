from django.urls import path, include
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('novo/', views.criar_projeto, name='criar_projeto'),
    path('editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('excluir/<int:id>/', views.excluir_projeto, name='excluir_projeto'),
    path('detalhar/<int:id>/', views.detalhar_projeto, name='detalhar_projeto'),
    path('<int:projeto_id>/tarefas/', include('tarefas.urls', namespace='tarefas')),

]
