from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='profile', blank=False, null=True, default='profile/filename.jpg')
    email = models.CharField(max_length=150)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    name = models.ManyToManyField(Profile)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='posts', default='profile/filename.jpg')
    post_msg = models.TextField()
    post_date = models.DateTimeField()
