from rest_framework import serializers
from medicar.agenda.models import Agenda


class AgendaSerializer(serializers.ModelSerializer):
    medico = serializers.SerializerMethodField('get_nome_from_medico')

    class Meta:
        model = Agenda
        fields = ['medico', 'dia', 'horario']

    def get_nome_from_medico(self, agenda):
        return agenda.medico.nome