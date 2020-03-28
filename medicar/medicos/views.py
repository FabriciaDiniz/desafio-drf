from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from medicar.especialidades.models import Especialidade
from medicar.medicos.serializers import MedicosSerializer

def get_medicos(request):
    serializer = MedicosSerializer(Especialidade.objects.all(), many=True)

    response = Response(serializer.data)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}

    return response
