from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    fullname = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'fullname', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
