from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Productos'
        verbose_name_plural = 'Categorías de Productos'


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='categoría',
    )
    nombre = models.CharField(max_length=100, db_index=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        base = f'{self.nombre} - ${self.precio}'
        if self.categoria:
            return f'{self.categoria} - {base}'
        return base

    class Meta:
        unique_together = ('categoria', 'nombre')
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Vendedor(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='vendedor'
    )
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='imagenes_perfil', blank=True, null=True)

    def __str__(self):
        return self.usuario.username


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ('-fecha_venta',)

    def __str__(self):
        return f"{self.vendedor.usuario.username} - {self.producto.nombre} - ${self.precio_total}"

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError('La cantidad no puede ser superior al stock')

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
