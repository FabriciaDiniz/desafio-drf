from django.db import models

from medicar.especialidades.models import Especialidade


class Medico(models.Model):
    def __str__(self):
        return self.nome
    
    nome = models.CharField(max_length=200, unique=False, null=False)
    crm = models.CharField(max_length=13, unique=True, null=False)
    email = models.CharField(max_length=200, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, max_length=50, on_delete=models.CASCADE, null=True, blank=True)

