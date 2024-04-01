from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class CreateStatusForm(ModelForm):

    class Meta:
        model = Status
        fields = ('name',)
      
class UpdateStatusForm(CreateStatusForm):
    pass
    #def clean_name(self):
    #    name = self.cleaned_data.get("name")
    #    return name
