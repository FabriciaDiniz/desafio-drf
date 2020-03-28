from rest_framework import serializers

from medicar.medicos.models import Medico
from medicar.especialidades.serializers import EspecialidadesSerializer


class MedicosSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadesSerializer()

    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade']
