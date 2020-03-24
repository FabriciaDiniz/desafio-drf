from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from medicar.home.serializers import TuplaSerializer
from medicar.home.common import ESPECIALIDADE_CHOICES

def especialidades(request):
    serializer = TuplaSerializer(ESPECIALIDADE_CHOICES)
    response = Response(serializer.data)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}

    return response
