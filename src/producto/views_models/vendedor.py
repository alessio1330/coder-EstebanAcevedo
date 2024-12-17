from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import VendedorForm
from ..models import Vendedor

# **** VENDEDOR - LIST VIEW


def vendedor_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Vendedor.objects.filter(usuario__username__icontains=busqueda)
    else:
        queryset = Vendedor.objects.all()
    return render(request, 'producto/vendedor_list.html', {'object_list': queryset})


# **** VENDEDOR - CREATE VIEW


def vendedor_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = VendedorForm()
    if request.method == 'POST':
        form = VendedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto:vendedor_list')
    return render(request, 'producto/vendedor_form.html', {'form': form})


# **** VENDEDOR - UPDATE VIEW


def vendedor_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Vendedor.objects.get(id=pk)
    if request.method == 'GET':
        form = VendedorForm(instance=query)
    if request.method == 'POST':
        form = VendedorForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            form.save()
            return redirect('producto:vendedor_list')
    return render(request, 'producto/vendedor_form.html', {'form': form})


# **** VENDEDOR - DETAIL VIEW


def vendedor_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Vendedor.objects.get(id=pk)
    return render(request, 'producto/vendedor_detail.html', {'object': query})


# **** VENDEDOR - DELETE VIEW


def vendedor_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Vendedor.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('producto:vendedor_list')
    return render(request, 'producto/vendedor_confirm_delete.html', {'object': query})
