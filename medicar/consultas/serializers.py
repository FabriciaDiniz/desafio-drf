from datetime import date

from rest_framework import serializers

from medicar.consultas.models import Consulta
from medicar.medicos.serializers import MedicosSerializer
from medicar.agenda.serializers import AgendaSerializer


class ConsultaSerializer(serializers.ModelSerializer):

    agenda = AgendaSerializer()
    dia = agenda.data
    horario = agenda.horario
    medico = agenda.medico

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'data_agendamento', 'medico']
