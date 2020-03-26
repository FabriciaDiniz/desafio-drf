from _datetime import date
from django.db import models
from medicar.medicos.models import Medico

class Agenda(models.Model):
    def __str__(self):
        data_agenda = "Agenda para %s - %s" % (self.medico.nome,self.dia)
        return data_agenda
    
    medico = models.ForeignKey(Medico, max_length=200, on_delete=models.DO_NOTHING, null=False)
    dia = models.DateField(default=date.today, null=False)
    horarios = models.CharField(max_length=12, choices=HORARIOS_CHOICES, null=False, default='8')

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

