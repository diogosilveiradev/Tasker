from django import forms
from .models import Projeto, Tarefa

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']


