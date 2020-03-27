from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from medicar.agenda.models import Agenda
from medicar.agenda.serializers import AgendaSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_detalhe_agenda(request):

    serializer = AgendaSerializer(request.data)
    data = {}
    try:
        agenda = serializer.save()
        data['response'] = 'Nova agenda cadastrada com sucesso'
        data['medico'] = agenda.medico.nome
        data['horario'] = str(agenda.horarios)
    except ValidationError as e:
        data = e.ErrorDetail
    return Response(data)
