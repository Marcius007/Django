from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='profile', blank=False, null=True, default='profile/filename.jpg')
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
