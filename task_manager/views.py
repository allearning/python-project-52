from django.views.generic import TemplateView
from django.contrib.auth.views  import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class MyLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')


def logout_view(request):
    logout(request)