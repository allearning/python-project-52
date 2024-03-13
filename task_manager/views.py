from django.views.generic import TemplateView
from django.contrib.auth.views  import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

class IndexView(TemplateView):
    template_name = "index.html"


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')
    success_message = _('You have logged in')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')
