from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.authtoken')),
    path('agendas/', include('medicar.agenda.urls')),
    path('users/', include('medicar.users.urls', 'user_api')),
    path('especialidades/', include('medicar.especialidades.urls')),
    path('medicos/', include('medicar.medicos.urls')),
    path('consultas/', include('medicar.consultas.urls'))
]
