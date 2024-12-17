from django.urls import path

from .views import index
from .views_models import categoria, producto, vendedor, venta

app_name = 'producto'

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += [
    path('categoria/list/', categoria.categoria_list, name='categoria_list'),
    path('categoria/create/', categoria.categoria_create, name='categoria_create'),
    path(
        'categoria/update/<int:pk>', categoria.categoria_update, name='categoria_update'
    ),
    path(
        'categoria/detail/<int:pk>', categoria.categoria_detail, name='categoria_detail'
    ),
    path(
        'categoria/delete/<int:pk>', categoria.categoria_delete, name='categoria_delete'
    ),
]

urlpatterns += [
    path('producto/list/', producto.ProductoListView.as_view(), name='producto_list'),
    path(
        'producto/create/',
        producto.ProductoCreateView.as_view(),
        name='producto_create',
    ),
    path(
        'producto/update/<int:pk>',
        producto.ProductoUpdateView.as_view(),
        name='producto_update',
    ),
    path(
        'producto/detail/<int:pk>',
        producto.ProductoDetailView.as_view(),
        name='producto_detail',
    ),
    path(
        'producto/delete/<int:pk>',
        producto.ProductoDeleteView.as_view(),
        name='producto_delete',
    ),
]

urlpatterns += [
    path('vendedor/list/', vendedor.vendedor_list, name='vendedor_list'),
    path('vendedor/create/', vendedor.vendedor_create, name='vendedor_create'),
    path(
        'vendedor/update/<int:pk>', vendedor.vendedor_update, name='vendedor_update'
    ),
    path(
        'vendedor/detail/<int:pk>', vendedor.vendedor_detail, name='vendedor_detail'
    ),
    path(
        'vendedor/delete/<int:pk>', vendedor.vendedor_delete, name='vendedor_delete'
    ),
]

urlpatterns += [
    path('venta/list/', venta.venta_list, name='venta_list'),
    path('venta/create/', venta.venta_create, name='venta_create'),
    path(
        'venta/update/<int:pk>', venta.venta_update, name='venta_update'
    ),
    path(
        'venta/detail/<int:pk>', venta.venta_detail, name='venta_detail'
    ),
    path(
        'venta/delete/<int:pk>', venta.venta_delete, name='venta_delete'
    ),
]
