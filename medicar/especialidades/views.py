from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from medicar.especialidades.models import Especialidade
from medicar.especialidades.serializers import EspecialidadesSerializer


class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualizar especilidades
    """
    serializer_class = EspecialidadesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Opcionalmente filtra pelo parâmetro 'nome' passado na URL
        """
        queryset = Especialidade.objects.all()
        nome = self.request.query_params.get('search')
        if nome is not None:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset
