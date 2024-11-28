from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
