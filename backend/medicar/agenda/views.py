from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from medicar.agenda.models import Agenda
from medicar.agenda.serializers import AgendaSerializer


#TODO: só permitir create para admin
class AgendaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar agendas
    """
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # TODO: fazer filtro de horarios funcionar
        queryset = Agenda.objects\
            .filter(dia__gte=datetime.today())
            # .filter(horarios__hora__gte=datetime.now())
        medico_id = self.request.query_params.getlist('medico')
        especialidade_id = self.request.query_params.getlist('especialidade')
        data_inicio = self.request.query_params.get('data_inicio')
        data_final = self.request.query_params.get('data_final')

        for m_id in medico_id:
            queryset = queryset.filter(medico__id=m_id)
        for e_id in especialidade_id:
            queryset = queryset.filter(especialidade__id=e_id)
        if data_inicio is not None:
            queryset = queryset.filter(dia__gte=data_inicio.date())
        if data_final is not None:
            queryset = queryset.filter(dia__lte=data_final.date())

        return queryset
