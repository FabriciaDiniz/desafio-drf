from rest_framework import serializers

from medicar.agenda.models import Agenda
from medicar.medicos.serializers import MedicoSerializer


class AgendaSerializer(serializers.ModelSerializer):

    # TODO: fazer campo de horários ficar no formato correto
    medico = MedicoSerializer()
    horarios = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='hora'
    )

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']
