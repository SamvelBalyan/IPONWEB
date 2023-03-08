from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        fields = ["username","first_name","last_name","email", "password1", "password2"]
        model = User


class AvatarForm(forms.Form):
    avatar = forms.ImageField(label='New Avatar')
