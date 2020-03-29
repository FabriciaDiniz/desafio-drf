from rest_framework import viewsets

from medicar.especialidades.models import Especialidade
from medicar.especialidades.serializers import EspecialidadesSerializer


class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualizar especilidades
    """
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadesSerializer
