from rest_framework import serializers

from medicar.medicos.models import Medico
from medicar.especialidades.serializers import EspecialidadeSerializer


class MedicoSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadeSerializer()

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']
