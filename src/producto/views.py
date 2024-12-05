from django.shortcuts import render

from . import forms, models


def index(request):
    return render(request, 'producto/index.html')


def categoria_list(request):
    categorias = models.Categoria.objects.all()
    return render(request, 'producto/categoria_list.html', {'categorias': categorias})


def categoria_create(request):
    form = forms.CategoriaForm()
    return render(request, 'producto/categoria_form.html', {'form': form})
