from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from medicar.medicos.models import Medico
from medicar.medicos.serializers import MedicosSerializer


class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualizar médicos
    """
    serializer_class = MedicosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Medico.objects.all()
        nome = self.request.query_params.get('search')
        especialidades = self.request.query_params.getlist('especialidade')
        if nome is not None:
            queryset = queryset.filter(nome__icontains=nome)
        for especialidade in especialidades:
            queryset = queryset.filter(especialidade__id=especialidade)

        return queryset
