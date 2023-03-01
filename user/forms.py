from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="Parol")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'label-input100'})
        self.fields['password'].widget.attrs.update({'class': 'label-input100'})