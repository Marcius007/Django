from django import forms
from .models import Profile, Post, User,Work_site
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, ModelForm
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus.widgets import DatePickerInput


help_text = 'Your password can’t be too similar to your other personal information.' + 'Your password must contain at least 8 characters.\n' \
            'Your password can’t be a commonly used password.\n Your password can’t be entirely numeric.'
class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat password")

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


class CreatPost(ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'title', 'picture', 'post_msg', 'post_date']


class MyDatePickerInput(DatePickerInput):
    template_name = 'date_picker.html'


class PostUpdateForm(ModelForm):

    class Meta:
        model = Post
        fields = [
            'post_label', "title", 'picture', 'post_msg', 'post_date'
            ]
        widgets = {
            'post_date': MyDatePickerInput(format='%m/%d/%Y')
        }


class UserUpdateForm(ModelForm):

    password = forms.CharField(disabled=True)
    last_login = forms.DateTimeField(disabled=True)
    date_joined = forms.DateTimeField(disabled=True)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['link'] = Work_site.objects.link.all()
    #     context['facebook'] = Work_site.objects.face_book.all()
    #     context['linkedin'] = Work_site.objects.linked_in.all()
    #     return context

    # CHOICES = forms.CharField()
    # work_id = forms.CharField(widget=forms.RadioSelect(), choices=CHOICES)
    class Meta:
        model = User
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["work_id"] = forms.ChoiceField(choices=((self.work_id.id, self.work_id.link),
                                                                 (self.work_id.id, self.work_id.face_book),
                                                                 (self.work_id.id, self.work_id.linked_in)))


