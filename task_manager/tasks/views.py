from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import FormMixin

from task_manager.tasks.forms import CreateTaskForm, UpdateTaskForm, TaskFilterForm
from task_manager.tasks.models import Task
from task_manager.users.views import LoginMessageMixin, MyUserControlMixin


# Create your views here.
class IndexTasksView(LoginMessageMixin, FormMixin, ListView):

    template_name = "tasks/index.html"
    model = Task
    form_class = TaskFilterForm
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks')
    }
    permission_denied_message = _('You are not logged in! Please Log in.')

    def get_form(self, form_class=None) -> forms.BaseForm:
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(data=self.request.GET) if self.request.GET else form_class()
        return form

    def get_queryset(self):
        filters = {field+'_id': self.request.GET.get(field, None) for field in ('status', 'executor') if self.request.GET.get(field, None)}
        if self.request.GET.get('self_tasks', None):
            filters['author_id'] = self.request.user.id
        new_context = Task.objects.filter(**filters)
        return new_context

class TaskCreateView(LoginMessageMixin, SuccessMessageMixin, CreateView):
    """
    Create new task.
    """
    template_name = "tasks/create.html"

    form_class = CreateTaskForm

    success_url = reverse_lazy('tasks')
    success_message = _('Task succesfully created')
    permission_denied_message = _('You are not logged in! Please Log in.')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginMessageMixin, SuccessMessageMixin, UpdateView):
    """
    Update task.
    """
    template_name = "tasks/update.html"
    model = Task

    form_class = UpdateTaskForm

    success_url = reverse_lazy('tasks')
    success_message = _('Task succesfully changed')
    permission_denied_message = _('You are not logged in! Please Log in.')


class TaskDeleteView(LoginMessageMixin, MyUserControlMixin, SuccessMessageMixin, DeleteView):
    """
    Delete task.
    """    
    template_name = "tasks/remove.html"
    model = Task

    def is_user_correct(self, user):
        return user.id == self.get_object().author_id
    
    success_url = reverse_lazy('tasks')
    success_message = _('Task succesfully deleted')
    wrong_user_message = _('Only creator can delete task')
    wrong_user_url = reverse_lazy('tasks')
    permission_denied_message = _('You are not logged in! Please Log in.')


class TaskDetailsView(DetailView):
    template_name = "tasks/details.html"
    model = Task
    extra_context = {
        'title': _('Task overview')
    }