import unicodedata

from django.core.exceptions import ValidationError
from django.db import models


class Categoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Productos'
        verbose_name_plural = 'Categorías de Productos'

    def validate_unique(self, exclude=None):
        """
        Valida que el campo 'nombre' sea único, ignorando tildes y mayúsculas.
        """
        super().validate_unique(exclude)
        texto_normalizado = unicodedata.normalize('NFD', self.nombre)
        texto_normalizado = texto_normalizado.encode('ascii', 'ignore').decode('utf-8').lower()
        query = Categoria.objects.filter(nombre__iexact=texto_normalizado)

        if self.pk:  # Excluir la instancia actual en caso de actualización
            query = query.exclude(pk=self.pk)
        if query.exists():
            raise ValidationError(
                f'Ya existe considerando tildes y mayúsculas en el campo {self.nombre}.'
            )


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='categoría'
    )
    nombre = models.CharField(max_length=100, db_index=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        if self.categoria:
            return f'{self.categoria} - {self.nombre}'
        return self.nombre

    class Meta:
        unique_together = ('categoria', 'nombre')
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
