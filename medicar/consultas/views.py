from datetime import datetime

from rest_framework import viewsets

from medicar.consultas.models import Consulta
from medicar.consultas.serializers import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para trabalhar com consultas
    """
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Consulta.objects.filter(paciente=user)\
            .exclude(horario__hora__lt=datetime.now().time())\
            .exclude(agenda__dia__lt=datetime.today())

        return qs
