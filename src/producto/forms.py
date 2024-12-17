from django import forms

from .models import Categoria, Producto, Vendedor, Venta


def validar_nombre(nombre: str):
    if len(nombre) < 3:
        raise forms.ValidationError('La longitud debe ser mayor a 3 caracteres')
    if not nombre.isalpha():
        raise forms.ValidationError('Debe contener caracteres alfabéticos')
    return nombre


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')
        return validar_nombre(nombre)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio', 'stock']

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')
        return validar_nombre(nombre)


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['usuario', 'celular', 'avatar']


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['vendedor', 'producto', 'cantidad']
