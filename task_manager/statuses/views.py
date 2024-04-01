from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from task_manager.statuses.forms import CreateStatusForm, UpdateStatusForm
from task_manager.statuses.models import Status


# Create your views here.
class IndexStatusesView(LoginRequiredMixin, ListView):
    template_name = "statuses/index.html"
    model = Status
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses')
    }
    permission_denied_message = _('You are not logged in! Please Log in.')



class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create new status.
    """
    template_name = "statuses/create.html"

    form_class = CreateStatusForm

    success_url = reverse_lazy('statuses')
    success_message = _('Status succesfully created')
    permission_denied_message = _('You are not logged in! Please Log in.')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update status.
    """
    template_name = "statuses/update.html"
    model = Status

    form_class = UpdateStatusForm

    success_url = reverse_lazy('statuses')
    success_message = _('Status succesfully changed')
    permission_denied_message = _('You are not logged in! Please Log in.')

class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Delete status.
    """
    template_name = "statuses/remove.html"
    model = Status

    success_url = reverse_lazy('statuses')
    success_message = _('Status succesfully deleted')
    permission_denied_message = _('You are not logged in! Please Log in.')