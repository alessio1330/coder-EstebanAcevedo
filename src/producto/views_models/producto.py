from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from ..forms import ProductoForm
from ..models import Producto


class ProductoListView(ListView):
    model = Producto

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            queryset = Producto.objects.filter(nombre__icontains=busqueda)
        else:
            queryset = Producto.objects.all()
        return queryset


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:producto_list')


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:producto_list')


class ProductoDetailView(DetailView):
    model = Producto


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:producto_list')
