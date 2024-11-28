from django.shortcuts import render

from .models import Cliente


def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes})
