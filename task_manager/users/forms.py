from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1', 'password2'
                  )
        
class UpdateUserForm(CreateUserForm):

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username
    