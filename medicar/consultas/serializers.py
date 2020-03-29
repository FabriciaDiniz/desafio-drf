from datetime import date

from rest_framework import serializers

from medicar.consultas.models import Consulta
from medicar.agenda.serializers import AgendaSerializer


class ConsultaSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    agenda_dia = serializers.SerializerMethodField()
    agenda_horario = serializers.SerializerMethodField()
    agenda_medico = serializers.SerializerMethodField()

    def get_agenda_dia(self, obj):
        return obj.agenda.dia

    def get_agenda_horario(self, obj):
        return obj.agenda.horarios

    def get_agenda_medico(self, obj):
        return obj.agenda.medico

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
