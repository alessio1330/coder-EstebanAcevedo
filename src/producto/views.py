from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import CategoriaForm
from .models import Categoria


def index(request):
    return render(request, 'producto/index.html')


# **** CATEGORIA - LIST VIEW


def categoria_list(request: HttpRequest) -> HttpResponse:
    queryset = Categoria.objects.all()
    return render(request, 'producto/categoria_list.html', {'object_list': queryset})


# **** CATEGORIA - CREATE VIEW


def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_form.html', {'form': form})


# **** CATEGORIA - UPDATE VIEW


def categoria_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    if request.method == 'GET':
        form = CategoriaForm(instance=query)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_form.html', {'form': form})


# **** CATEGORIA - DETAIL VIEW


def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    return render(request, 'producto/categoria_detail.html', {'object': query})


# **** CATEGORIA - DELETE VIEW


def categoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_confirm_delete.html', {'object': query})
