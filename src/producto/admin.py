from django.contrib import admin

from . import models

admin.site.register(models.Categoria)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'precio', 'stock')
    list_display_links = ('nombre',)
    list_filter = ('categoria',)
    search_fields = ('categoria', 'nombre')


admin.site.register(models.Vendedor)


@admin.register(models.Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'producto', 'cantidad', 'precio_total', 'fecha_venta')
