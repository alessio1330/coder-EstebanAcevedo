from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse('¡Hola Django!')


def saludar_con_etiqueta(request):
    return HttpResponse('<h1> Este es el título de mi App </h1>')
