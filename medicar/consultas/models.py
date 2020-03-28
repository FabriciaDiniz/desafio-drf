from datetime import date
from rest_framework.exceptions import ValidationError

from django.db import models

from medicar.agenda.models import Agenda
from medicar.agenda.models import Horario
from medicar.users.models import User


class Consulta(models.Model):
    def __str__(self):
        data_consulta = self.medico.nome + '-' + str(self.horario)
        return data_consulta

    horario = models.ForeignKey(Horario, on_delete=models.DO_NOTHING, null=False)
    data_agendamento = models.DateField(auto_now=True, null=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, null=False)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['-agenda', '-horario']
        unique_together = ('paciente', 'agenda', 'horario')

    def clean(self):
        if self.dia < date.today():
            raise ValidationError('Consulta não pode ser agendada para data passada')
        consultas = Consulta.objects.filter(horario=self.horario).filter(agenda=self.agenda)
        if consultas:
            raise ValidationError('Já existe uma consultas marcada para este dia e horário')

    def save(self):
        self.clean()
        super.save()

