from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
@user_passes_test(is_staff)
def criar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form, 'titulo': 'Criar Usuário'})

@login_required
@user_passes_test(is_staff)
def editar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UserChangeForm(instance=usuario)
    return render(request, 'usuarios/form_usuario.html', {'form': form, 'titulo': 'Editar Usuário'})

@login_required
@user_passes_test(is_staff)
def excluir_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('usuarios:lista_usuarios')
    return render(request, 'usuarios/confirma_exclusao.html', {'usuario': usuario})
