from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

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


class UserCreateView(CreateView):
    """
    Create new user.
    """
    template_name = "users/signin.html"

    form_class = CreateUserForm

    success_url = reverse_lazy('login')
    # success_message = _('User is successfully registered')


class MyUserControlMixin:

    login_url = settings.LOGIN_URL
    wrong_user_url = login_url

    not_logged_message = _('You are not logged in! Please Log in.')
    lincorrect_user_message = _('You have no rights to edit another user')

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.__class__.not_logged_message)
            return redirect(self.__class__.login_url, self.request)

        if self.request.user.id != self.kwargs['pk']:
            messages.error(self.request, self.__class__.lincorrect_user_message)
            return redirect(self.__class__.wrong_user_url, self.request)
        
        return super().get(self, *args, **kwargs)    


class UserUpdateView(MyUserControlMixin, UpdateView):
    """
    Update user.
    """
    template_name = "users/update.html"
    model = User

    form_class = UpdateUserForm

    login_url = reverse_lazy('login')
    wrong_user_url = reverse_lazy('users')

    success_url = reverse_lazy('users')
    # success_message = _('User is successfully registered')


class UserDeleteView(MyUserControlMixin, DeleteView):
    """
    Delete user.
    """
    template_name = "users/remove.html"
    model = User

    login_url = reverse_lazy('login')
    wrong_user_url = reverse_lazy('users')

    success_url = reverse_lazy('index')
    # success_message = _('User is successfully registered')
