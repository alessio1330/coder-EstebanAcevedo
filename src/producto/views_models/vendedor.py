from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import VendedorForm
from ..models import Vendedor


class VendedorListView(ListView):
    model = Vendedor

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Vendedor.objects.filter(usuario__username__icontains=busqueda)
        return Vendedor.objects.all()


class VendedorCreateView(CreateView):
    model = Vendedor
    form_class = VendedorForm
    success_url = reverse_lazy('producto:vendedor_list')


class VendedorUpdateView(UpdateView):
    model = Vendedor
    form_class = VendedorForm
    success_url = reverse_lazy('producto:vendedor_list')


class VendedorDetailView(DetailView):
    model = Vendedor


class VendedorDeleteView(DeleteView):
    model = Vendedor
    success_url = reverse_lazy('producto:vendedor_list')
