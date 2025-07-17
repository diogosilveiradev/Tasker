from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
]
