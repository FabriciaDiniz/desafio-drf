from django.urls import path

from medicar.agenda.views import api_detalhe_agenda


app_name = 'agenda'

urlpatterns = [
    path('<slug>/', api_detalhe_agenda, name='detalhe'),
]