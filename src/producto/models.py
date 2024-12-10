import unicodedata

from django.core.exceptions import ValidationError
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
