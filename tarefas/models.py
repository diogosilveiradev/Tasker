from django.db import models
from projetos.models import Projeto  

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    prazo = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'projetos_tarefa'  
