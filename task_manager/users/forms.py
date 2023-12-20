from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label=_("First Name"), max_length=100)
    last_name = forms.CharField(label=_("Last name"), max_length=100)
    field_order = ['first_name', 'last_name', 'username', 'password1', 'password2']