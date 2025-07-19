from django import forms
from projetos.models import Tarefa

class TarefaForm(forms.ModelForm):
    prazo = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao','prazo', 'concluida']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'prazo': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'concluida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
