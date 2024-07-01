from typing import Any
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class RegistroUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class CustomUserCreationForm(UserCreationForm):
    # Customizing the username field
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='awa de uwu',
        validators=[EmailValidator()],  # Example customization: enforce email format
        error_messages={
            'required': "Username is required.",
            'unique': "A user with that username already exists.",
        },
    )