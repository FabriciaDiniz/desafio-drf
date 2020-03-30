import json
from json import JSONEncoder
from datetime import date

from rest_framework.exceptions import ValidationError

from django.db import models

from medicar.medicos.models import Medico


class Horario(models.Model):
    #TODO: formatar a hora do jeito correto
    def __str__(self):
        return str(self.hora)

    def to_json(self):
        return json.dumps(
            default=lambda x: getattr(x, '__dict__', str(x))
        )

    hora = models.TimeField(null=False)


class Agenda(models.Model):
    def __str__(self):
        data_agenda = self.medico.nome + ' ' + str(self.dia)
        return data_agenda

    medico = models.ForeignKey(Medico, max_length=200, on_delete=models.CASCADE, null=False)
    dia = models.DateField(default=date.today, null=False)
    horarios = models.ManyToManyField(Horario)

    class Meta:
        ordering = ['-dia']
        unique_together = ('medico', 'dia')

    # TODO: fazer validações funcionarem
    def clean(self):
        if self.dia < date.today():
            raise ValidationError('Agenda não pode ser criada para data passada')
