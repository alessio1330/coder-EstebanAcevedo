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
        fields = ['producto', 'cantidad']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VentaForm, self).__init__(*args, **kwargs)
        if self.user:
            vendedor = Vendedor.objects.get(usuario=self.user)
            self.fields['vendedor'] = forms.CharField(
                initial=vendedor.usuario.username,
                widget=forms.TextInput(attrs={'readonly': 'readonly'}),
            )

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        producto = self.cleaned_data.get('producto')
        if cantidad and producto and cantidad > producto.stock:
            raise forms.ValidationError('La cantidad no puede ser superior al stock')
        return cantidad
