from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import VentaForm
from ..models import Venta


class VentaListView(ListView):
    model = Venta

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Venta.objects.filter(
                vendedor__usuario__username__icontains=busqueda
            ) | Venta.objects.filter(producto__nombre__icontains=busqueda)
        return Venta.objects.all()


class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('producto:venta_list')

    def form_valid(self, form):
        venta = form.save(commit=False)
        producto = form.cleaned_data['producto']
        cantidad = form.cleaned_data['cantidad']
        venta.precio_total = producto.precio * cantidad
        venta.save()
        return super().form_valid(form)


class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('producto:venta_list')

    def form_valid(self, form):
        venta = form.save(commit=False)
        producto = form.cleaned_data['producto']
        cantidad = form.cleaned_data['cantidad']
        venta.precio_total = producto.precio * cantidad
        venta.save()
        return super().form_valid(form)


class VentaDetailView(DetailView):
    model = Venta


class VentaDeleteView(DeleteView):
    model = Venta
    success_url = reverse_lazy('producto:venta_list')
