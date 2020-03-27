from django.contrib import admin
from medicar.agenda.models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    # prepop fields não aceita datetime nem fk
    prepopulated_fields = {"slug": ("id",)}


class AgendaAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Agenda, AgendaAdmin)