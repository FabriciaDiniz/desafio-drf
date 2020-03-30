from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from medicar.consultas.models import Consulta
from medicar.consultas.serializers import ConsultaSerializer, ConsultaCreateSerializer


#TODO: implementar delete
class ConsultaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para trabalhar com consultas
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Consulta.objects.filter(paciente=user)\
            .exclude(horario__hora__lt=datetime.now().time())\
            .exclude(agenda__dia__lt=datetime.today())

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ConsultaCreateSerializer
        return ConsultaSerializer
