from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager import settings
from task_manager.users.forms import CreateUserForm, UpdateUserForm

# Create your views here.


class IndexUsersView(ListView):
    template_name = "users/index.html"
    model = User
    context_object_name = 'users'
    extra_context = {
        'title': _('Users')
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Create new user.
    """
    template_name = "users/signup.html"

    form_class = CreateUserForm

    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')


class LoginMessageMixin(LoginRequiredMixin):
    not_logged_message = _('You are not logged in! Please Log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.__class__.not_logged_message)
        return super().dispatch(request, *args, **kwargs)
    

class MyUserControlMixin:
    wrong_user_url = reverse_lazy('users')
    wrong_user_message = _('You have no rights to edit another user')

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.kwargs['pk']:
            messages.error(
                request, self.__class__.wrong_user_message)
            return redirect(self.__class__.wrong_user_url, request)

        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(LoginMessageMixin, MyUserControlMixin, SuccessMessageMixin, UpdateView):
    """
    Update user.
    """
    template_name = "users/update.html"
    model = User

    form_class = UpdateUserForm

    login_url = reverse_lazy('login')
    wrong_user_url = reverse_lazy('users')

    success_url = reverse_lazy('users')
    success_message = _('User succesfully changed')


class UserDeleteView(LoginMessageMixin, MyUserControlMixin, SuccessMessageMixin, DeleteView):
    """
    Delete user.
    """
    template_name = "users/remove.html"
    model = User

    login_url = reverse_lazy('login')
    wrong_user_url = reverse_lazy('users')

    success_url = reverse_lazy('users')
    success_message = _('User succesfully deleted')
