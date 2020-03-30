from abc import ABC
from datetime import datetime

from rest_framework import serializers

from medicar.consultas.models import Consulta
from medicar.agenda.models import Agenda, Horario


class ConsultaSerializer(serializers.ModelSerializer):

    dia = serializers.SerializerMethodField()
    horario = serializers.SerializerMethodField()
    medico = serializers.SerializerMethodField()

    def get_dia(self, obj):
        return obj.agenda.dia

    def get_horario(self, obj):
        return obj.agenda.horarios

    def get_medico(self, obj):
        return obj.agenda.medico

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']


class ConsultaCreateSerializer(serializers.BaseSerializer, ABC):

    # TODO: fazer validações funcionarem
    def validate_horario(self, value):
        if self.data.agenda.data == datetime.date.today():
            if value < datetime.now().today():
                raise serializers.ValidationError(
                    "Consulta não pode ser agendada para horário passado"
                )

    def to_internal_value(self, data):
        agenda_id = data.get('agenda_id')
        horario = data.get('horario')

        if not agenda_id:
            raise serializers.ValidationError({
                'agenda_id': 'Campo obrigatório.'
            })
        if not horario:
            raise serializers.ValidationError({
                'horario': 'Campo obrigatório.'
            })

        agenda = Agenda.objects.get(id=agenda_id)

        horario_obj = Horario.objects.get(hora=horario)

        return {
            'agenda': agenda,
            'horario': horario_obj,
            'paciente': self.context['request'].user,
        }

    def to_representation(self, instance):
        # TODO: retornar valores corretos de acordo com os requisitos
        return {
            'id': instance.id,
            'horario': str(instance.horario),
        }

    def create(self, validated_data):
        return Consulta.objects.create(**validated_data)
