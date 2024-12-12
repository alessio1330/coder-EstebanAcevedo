from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomAuthenticationForm, CustomUserCreationForm


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        usuario = form.get_user()
        messages.success(
            self.request, f'Inicio de sesión exitoso ¡Bienvenido {usuario.username}!'
        )
        return super().form_valid(form)


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return super().form_valid(form)
