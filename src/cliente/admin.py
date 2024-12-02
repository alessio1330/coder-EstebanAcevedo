from django.contrib import admin

from . import models

admin.site.register(models.Pais)


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacimiento', 'pais_origen')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')
    list_filter = ('pais_origen',)
    date_hierarchy = 'nacimiento'
