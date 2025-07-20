from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(label='Membro da equipe', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

class UserBasicForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',  'email']
