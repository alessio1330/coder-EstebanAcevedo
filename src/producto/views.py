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


def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_form.html', {'form': form})
