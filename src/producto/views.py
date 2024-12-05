from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, 'producto/index.html')


def categoria_list(request):
    categorias = models.Categoria.objects.all()
    return render(request, 'producto/categoria_list.html', {'categorias': categorias})


def categoria_create(request):
    if request.method == 'GET':
        form = forms.CategoriaForm()
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_form.html', {'form': form})
