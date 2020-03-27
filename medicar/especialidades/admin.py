from django.contrib import admin
from medicar.especialidades.models import Especialidade


class EspecialidadeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


admin.site.register(Especialidade, EspecialidadeAdmin)
