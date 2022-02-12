from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, ModelForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(help_text=None, widget=forms.PasswordInput)
    password2 = forms.CharField(help_text=None, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateProfileForm(ModelForm):
    user_picture = forms.ImageField(required=None)

    class Meta:
        model = Profile
        fields = '__all__'
