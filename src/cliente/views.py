from django.shortcuts import render

from .models import Cliente, Pais


def index(request):
    return render(request, 'cliente/index.html')


def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'cliente/cliente_list.html', contexto)


def pais_list(request):
    paises = Pais.objects.all()
    contexto = {'paises': paises}
    return render(request, 'cliente/pais_list.html', contexto)
