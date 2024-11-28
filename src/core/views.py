from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse('¡Hola Django!')


def saludar_con_etiqueta(request):
    return HttpResponse('<h1> Este es el título de mi App </h1>')


def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f'{apellido}, {nombre}')


def index(request):
    return render(request, 'core/index.html')
