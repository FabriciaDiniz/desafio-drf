from django.urls import path
from medicar.users.views import registration_view

app_name = 'users'

urlpatterns = [
    path('register/', registration_view),
]