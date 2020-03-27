from rest_framework import serializers
from medicar.especialidades.models import Especialidade



class EspecialidadesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields=('id', 'nome')