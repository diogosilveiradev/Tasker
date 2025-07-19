from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from decorator_include import decorator_include
from django.contrib.auth.decorators import login_required
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', login_required(home), name='home'),

    path('usuarios/', include('usuarios.urls')),
    path('projetos/', include(('projetos.urls', 'projetos'), namespace='projetos')),
]
