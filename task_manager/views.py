from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from task_manager import forms


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def about(request):
    return render(request, 'about.html')


class LogView(LoginView):
    form_class = forms.LoginForm

    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'You have log in successfully.')
        return reverse_lazy('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):

    def post(self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('login')
