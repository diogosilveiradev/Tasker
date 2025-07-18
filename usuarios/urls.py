from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', lambda request: redirect('usuarios:lista_usuarios')),
    
    path('listar/', views.lista_usuarios, name='lista_usuarios'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
