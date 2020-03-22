from django.db import models
from medicar.home.common import ESPECIALIDADE_CHOICES

class Medico(models.Model):
    def __str__(self):
        return self.nome
    
    nome = models.CharField(max_length=200, unique=False, null=False)
    crm = models.CharField(max_length=13, unique=True, null=False)
    email = models.CharField(max_length=200, unique=True, null=True)
    telefone = models.CharField(max_length=11, unique=False,null=True)
    especialidade = models.CharField(max_length=20, choices=ESPECIALIDADE_CHOICES, null=True, default='CLINICA GERAL')
