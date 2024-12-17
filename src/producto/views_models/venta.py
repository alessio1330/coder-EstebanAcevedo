from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import VentaForm
from ..models import Venta

# **** VENTA - LIST VIEW


def venta_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Venta.objects.filter(
            vendedor__usuario__username__icontains=busqueda
        ) | Venta.objects.filter(producto__nombre__icontains=busqueda)
    else:
        queryset = Venta.objects.all()
    return render(request, 'producto/venta_list.html', {'object_list': queryset})


# **** VENTA - CREATE VIEW


def venta_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = VentaForm()
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            venta.precio_total = producto.precio * cantidad
            venta.save()
            return redirect('producto:venta_list')
    return render(request, 'producto/venta_form.html', {'form': form})


# **** VENTA - UPDATE VIEW


def venta_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Venta.objects.get(id=pk)
    if request.method == 'GET':
        form = VentaForm(instance=query)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=query)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            venta.precio_total = producto.precio * cantidad
            venta.save()
            return redirect('producto:venta_list')
    return render(request, 'producto/venta_form.html', {'form': form})


# **** VENTA - DETAIL VIEW


def venta_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Venta.objects.get(id=pk)
    return render(request, 'producto/venta_detail.html', {'object': query})


# **** VENTA - DELETE VIEW


def venta_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Venta.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('producto:venta_list')
    return render(request, 'producto/venta_confirm_delete.html', {'object': query})
