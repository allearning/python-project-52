from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.tasks.forms import CreateTaskForm, UpdateTaskForm
from task_manager.tasks.models import Task
from task_manager.users.views import LoginMessageMixin


# Create your views here.
class IndexTasksView(LoginMessageMixin, ListView):

    template_name = "tasks/index.html"
    model = Task
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks')
    }
    permission_denied_message = _('You are not logged in! Please Log in.')



class TaskCreateView(LoginMessageMixin, SuccessMessageMixin, CreateView):
    pass
    """
    Create new task.
    
    template_name = "tasks/create.html"

    form_class = CreateTaskForm

    success_url = reverse_lazy('tasks')
    success_message = _('Status succesfully created')
    permission_denied_message = _('You are not logged in! Please Log in.')
    """

class TaskUpdateView(LoginMessageMixin, SuccessMessageMixin, UpdateView):
    pass
    """
    Update task.
    
    template_name = "tasks/update.html"
    model = Task

    form_class = UpdateTaskForm

    success_url = reverse_lazy('tasks')
    success_message = _('Status succesfully changed')
    permission_denied_message = _('You are not logged in! Please Log in.')
    """
class TaskDeleteView(LoginMessageMixin, SuccessMessageMixin, DeleteView):
    pass
    """
    Delete task.
    
    template_name = "tasks/remove.html"
    model = Task

    success_url = reverse_lazy('tasks')
    success_message = _('Task succesfully deleted')
    permission_denied_message = _('You are not logged in! Please Log in.')
    """