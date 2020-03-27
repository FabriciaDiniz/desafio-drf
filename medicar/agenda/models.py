from datetime import date
from django.db import models

from medicar.medicos.models import Medico
from rest_framework.exceptions import ValidationError

class Agenda(models.Model):
    HORARIOS_CHOICES = [
        ('8', '8:00 - 9:00'),
        ('9', '9:00 - 10:00'),
        ('10', '10:00 - 11:00'),
        ('11', '11:00 - 12:00'),
        ('12', '12:00 - 13:00'),
        ('13', '13:00 - 14:00'),
        ('14', '14:00 - 15:00'),
        ('15', '15:00 - 16:00'),
        ('16', '16:00 - 17:00'),
        ('17', '17:00 - 18:00'),
        ('18', '18:00 - 19:00'),
        ('19', '19:00 - 20:00'),
        ('20', '20:00 - 21:00'),
    ]

    def __str__(self):
        data_agenda = self.medico.nome + '-' + str(self.dia)
        return data_agenda

    def validate_agenda_unica(self):
        agendas_por_medico = Agenda.objects.filter(medico=self.medico)

        for agenda in agendas_por_medico:
            if agenda.dia == self.dia:
                raise ValidationError('Não é possível criar duas agendas para o mesmo médico no mesmo dia')

    def validate_dia_posterior(self):
        if self.dia < date.today():
            raise ValidationError('Não é possível criar uma agenda para um dia passado')

    medico = models.ForeignKey(Medico, max_length=200, on_delete=models.CASCADE, null=False)
    dia = models.DateField(default=date.today, null=False)
    horarios = models.CharField(max_length=12, choices=HORARIOS_CHOICES, null=False, default='8')
    slug = models.SlugField(max_length=50, default=str(id))
