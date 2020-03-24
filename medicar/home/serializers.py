from rest_framework import serializers

class TuplaSerializer(serializers.Serializer):
    especialidades = serializers.SerializerMethodField()
    def get_especialidades(self, obj):
        objects = []
        for item in obj:
            objects.append(item[1])
        return objects