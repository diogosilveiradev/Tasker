from django.db import models
from projetos.models import Projeto

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, related_name='tarefas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    prazo = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
