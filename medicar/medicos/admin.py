from django.contrib import admin
from medicar.medicos.models import Medico

class MedicoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("crm")}

admin.site.register(Medico)