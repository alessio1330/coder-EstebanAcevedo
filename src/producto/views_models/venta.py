from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import VentaForm
from ..models import Vendedor, Venta


class VentaListView(ListView):
    model = Venta

    def get_queryset(self):
        """
        Obtiene el conjunto de consultas (queryset) para las ventas.

        Si se proporciona un parámetro de búsqueda en la solicitud GET, filtra las ventas
        por el nombre de usuario del vendedor o el nombre del producto que contengan
        el término de búsqueda (ignorando mayúsculas y minúsculas).

        Returns:
            QuerySet: Un conjunto de consultas de ventas filtradas según el término de búsqueda,
            o todas las ventas si no se proporciona un término de búsqueda.
        """
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

    def get_form_kwargs(self) -> dict:
        """
        Sobrescribe el método get_form_kwargs para incluir el usuario actual en los argumentos de
        palabra clave del formulario.
        Returns:
            dict: Los argumentos de palabra clave para el formulario, incluyendo el usuario actual.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form) -> HttpResponse:
        """
        Maneja la lógica cuando el formulario es válido.

        Este método se llama cuando el formulario ha sido validado correctamente.
        1. Guarda la venta sin confirmar la transacción en la base de datos.
        2. Asigna el vendedor basado en el usuario actual.
        3. Calcula el precio total de la venta.
        4. Actualiza el stock del producto y guarda tanto el producto como la venta.

        Args:
            form (Form): El formulario validado que contiene los datos de la venta.

        """
        venta = form.save(commit=False)
        venta.vendedor = Vendedor.objects.get(usuario=self.request.user)
        producto = form.cleaned_data['producto']
        cantidad = form.cleaned_data['cantidad']
        venta.precio_total = producto.precio * cantidad
        producto.stock -= cantidad
        producto.save()
        venta.save()
        return super().form_valid(form)


class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('producto:venta_list')

    def form_valid(self, form):
        """
        Método que se ejecuta cuando el formulario es válido.

        Args:
            form (Form): El formulario que contiene los datos de la venta.

        Returns:
            HttpResponse: La respuesta HTTP después de procesar el formulario válido.

        Este método realiza las siguientes acciones:
        1. Guarda la venta sin confirmar la transacción en la base de datos.
        2. Calcula el precio total de la venta multiplicando el precio del producto por la cantidad.
        3. Resta la cantidad vendida del stock del producto.
        4. Guarda los cambios en el producto.
        5. Guarda la venta.
        """
        venta = form.save(commit=False)
        producto = form.cleaned_data['producto']
        cantidad = form.cleaned_data['cantidad']
        venta.precio_total = producto.precio * cantidad
        producto.stock -= cantidad
        producto.save()
        venta.save()
        return super().form_valid(form)


class VentaDetailView(DetailView):
    model = Venta


class VentaDeleteView(DeleteView):
    model = Venta
    success_url = reverse_lazy('producto:venta_list')
