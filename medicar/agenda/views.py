from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from medicar.agenda.models import Agenda
from medicar.agenda.serializers import AgendaSerializer


class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualizar agendas
    """
    queryset = Agenda.objects.filter(dia__gte=datetime.today())
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]
