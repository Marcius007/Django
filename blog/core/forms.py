from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, ModelForm
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(help_text=None, widget=forms.PasswordInput)
    password2 = forms.CharField(help_text=None, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateProfileForm(ModelForm):
    user_picture = forms.ImageField(required=None, label='Picture', help_text='2MB max size')
    email = forms.EmailField(required=True, label='Email', help_text='You must include @ sign in your email')  # cia padarom kad butu tik asd@asd.com

    class Meta:
        model = Profile
        fields = '__all__'

    def clean(self):
        super(CreateProfileForm, self).clean()
        email = self.cleaned_data.get('email')

        if len(email) < 10:
            self.errors['email'] = self.error_class([
                'Minimum 10 chars required'
            ])
        return self.cleaned_data


class CreatPost:

    class Meta:
        model = Post
        fields = ['title', 'post_msg']
