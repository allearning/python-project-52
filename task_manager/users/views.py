from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .forms import CreateUserForm, UpdateUserForm

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
    #success_message = _('User is successfully registered')


class UserUpdateView(UpdateView):
    """
    Update user.
    """
    template_name = "users/update.html"
    model = User

    form_class = UpdateUserForm

    success_url = reverse_lazy('users')
    #success_message = _('User is successfully registered')


class UserDeleteView(DeleteView):
    """
    Delete user.
    """
    template_name = "users/remove.html"
    model = User

    success_url = reverse_lazy('index')
    #success_message = _('User is successfully registered')