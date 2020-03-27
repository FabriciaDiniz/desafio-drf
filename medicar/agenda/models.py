from datetime import date
from rest_framework.exceptions import ValidationError

from django.db import models

from medicar.medicos.models import Medico


class Horario(models.Model):
    def __str__(self):
        return str(self.hora)

    hora = models.TimeField()


class Agenda(models.Model):
    def __str__(self):
        data_agenda = self.medico.nome + '-' + str(self.dia)
        return data_agenda

    medico = models.ForeignKey(Medico, max_length=200, on_delete=models.CASCADE, null=False)
    dia = models.DateField(default=date.today, null=False)
    horarios = models.ManyToManyField(Horario)
    slug = models.SlugField(max_length=50, default=str(id))

    class Meta:
        ordering = ['-dia']
        unique_together = ('medico', 'dia')

    def clean(self):
        if self.dia < date.today():
            raise ValidationError('Agenda não pode ser criada para data passada')

    def save(self):
        self.clean()
        super.save()
