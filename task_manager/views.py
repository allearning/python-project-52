from django.views.generic import TemplateView
from django.contrib.auth.views  import LoginView, LogoutView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class MyLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')
