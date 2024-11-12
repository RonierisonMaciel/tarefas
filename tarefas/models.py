# tarefas/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-id']  # Exemplo: ordenar tarefas pela mais recente

    def clean(self):
        if Tarefa.objects.filter(titulo=self.titulo).exclude(id=self.id).exists():
            raise ValidationError('Você já possui uma tarefa com este título.')
