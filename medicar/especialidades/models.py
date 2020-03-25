from django.db import models

class Especialidade(models.Model):
    def __str__(self):
        return self.nome
    
    nome = models.CharField(max_length=200, unique=True, null=False)