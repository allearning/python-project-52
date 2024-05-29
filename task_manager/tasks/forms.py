from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

# from task_manager.labels.models import Label


class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(label=_('Status'), queryset=Status.objects.all(), required=False)
    executor = forms.ModelChoiceField(label=_('Executor'), queryset=User.objects.all(), required=False)
    self_tasks = forms.BooleanField(label=_('Self Tasks Only'), required=False)
    


class CreateTaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor',)
        
      
class UpdateTaskForm(CreateTaskForm):
    pass
    #def clean_name(self):
    #    name = self.cleaned_data.get("name")
    #    return name
