from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class CreateTaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ('name',)
      
class UpdateTaskForm(CreateTaskForm):
    pass
    #def clean_name(self):
    #    name = self.cleaned_data.get("name")
    #    return name
