from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(home), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('usuarios/', include('usuarios.urls')),
    path('projetos/', include(('projetos.urls', 'projetos'), namespace='projetos')),
    path('tarefas/', include(('tarefas.urls', 'tarefas'), namespace='tarefas')),
]
