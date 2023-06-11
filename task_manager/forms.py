from django.contrib.auth.forms import AuthenticationForm

from task_manager.users.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
            field.widget.attrs.update(placeholder=field.label)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        return self.cleaned_data['username'].lower()
