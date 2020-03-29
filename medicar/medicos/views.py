from rest_framework import viewsets

from medicar.medicos.models import Medico
from medicar.medicos.serializers import MedicosSerializer


class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualizar médicos
    """
    queryset = Medico.objects.all()
    serializer_class = MedicosSerializer
