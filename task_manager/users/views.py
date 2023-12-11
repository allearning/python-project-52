from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your views here.


class IndexUsersView(ListView):
    template_name = "users/index.html"
    model = User
    context_object_name = 'users'
    extra_context = {
        'title': _('Users')
    }
