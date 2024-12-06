from django.db import models


class Categoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Productos'
        verbose_name_plural = 'Categorías de Productos'
