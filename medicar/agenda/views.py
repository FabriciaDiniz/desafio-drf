from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from medicar.agenda.models import Agenda
from medicar.agenda.serializers import AgendaSerializer


@api_view(['GET'])
def api_detalhe_agenda(request, slug):
    try:
        agenda = Agenda.objects.get(slug=slug)
    except Agenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AgendaSerializer(agenda)
    return Response(serializer.data)