from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import ProductoForm
from ..models import Producto


class ProductoListView(ListView):
    model = Producto

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Producto.objects.filter(nombre__icontains=busqueda)
        return Producto.objects.all()


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Producto creado exitosamente')
        return super().form_valid(form)


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:producto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado exitosamente')
        return super().form_valid(form)


class ProductoDetailView(DetailView):
    model = Producto


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:producto_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Producto eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
