from django.contrib import admin

from . import models

admin.site.register(models.Categoria)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'precio', 'stock')
    list_display_links = ('nombre',)
    list_filter = ('categoria',)
    search_fields = ('categoria', 'nombre')
