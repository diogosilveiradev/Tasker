from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, UsuarioForm, UserBasicForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'usuarios/login.html')


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'usuarios/trocar_senha.html'
    success_url = reverse_lazy('usuarios:perfil')


def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser)
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


@login_required
@user_passes_test(is_superuser)
def criar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('usuarios:lista_usuarios')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/criar_usuario.html', {'form': form, 'titulo': 'Criar Usuário'})


@login_required
@user_passes_test(is_superuser)
def editar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/form_usuario.html', {'form': form, 'titulo': 'Editar Usuário'})


@login_required
@user_passes_test(is_superuser)
def excluir_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('usuarios:lista_usuarios')
    return render(request, 'usuarios/confirma_exclusao.html', {'usuario': usuario})


@login_required
def perfil(request):
    user = request.user
    if request.method == 'POST':
        if user.is_superuser:
            form = UsuarioForm(request.POST, instance=user)
        else:
            form = UserBasicForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('usuarios:perfil')
    else:
        if user.is_superuser:
            form = UsuarioForm(instance=user)
        else:
            form = UserBasicForm(instance=user)

    return render(request, 'usuarios/perfil.html', {'user_form': form})


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Usuário criado com sucesso! Agora faça login.')
            return redirect('usuarios:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})
