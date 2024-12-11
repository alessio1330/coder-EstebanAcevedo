from django.urls import path

from producto.views_models import categoria, producto

from . import views

app_name = 'producto'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('categoria/list/', categoria.categoria_list, name='categoria_list'),
    path('categoria/create/', categoria.categoria_create, name='categoria_create'),
    path('categoria/update/<int:pk>', categoria.categoria_update, name='categoria_update'),
    path('categoria/detail/<int:pk>', categoria.categoria_detail, name='categoria_detail'),
    path('categoria/delete/<int:pk>', categoria.categoria_delete, name='categoria_delete'),
]

urlpatterns += [
    path('producto/list/', producto.ProductoListView.as_view(), name='producto_list'),
    path('producto/create/', producto.ProductoCreateView.as_view(), name='producto_create'),
    path('producto/update/<int:pk>', producto.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/detail/<int:pk>', producto.ProductoDetailView.as_view(), name='producto_detail'),
    path('producto/delete/<int:pk>', producto.ProductoDeleteView.as_view(), name='producto_delete'),
]
