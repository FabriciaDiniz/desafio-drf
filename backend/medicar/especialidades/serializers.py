from rest_framework import serializers

from medicar.especialidades.models import Especialidade


class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = ('id', 'nome')
