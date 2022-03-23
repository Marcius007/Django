from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='profile', blank=False, null=True, default='profile/filename.jpg')
    email = models.CharField(max_length=150)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


POST_LABELS = (
    ("NEW", "New"),
    ("TOP", "Top"),
    ("BEST", "Best"),
)


class Post(models.Model):
    name = models.ManyToManyField(Profile)
    post_label = models.CharField(max_length=4, choices=POST_LABELS, default="New", null=True, blank=True)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='posts', default='profile/filename.jpg')
    post_msg = models.TextField()
    post_date = models.DateTimeField()


PROFESSION_CHOISE = (
    ("DOCTOR", "Doctor"),
    ("POLICE-MAN", "Police-man"),
    ("OWNER", "Owner"),
    ("WEB-DEV", "Web-dev"),
    ("DATA-ANALYST", "Data-analyst"),
)


class Work_site(models.Model):
    user_work_link = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(max_length=150, blank=True)
    face_book = models.CharField(max_length=150, default='facebook.com', blank=True)
    linked_in = models.CharField(max_length=150, default='linkedin.com', blank=True)

    def __str__(self):
        return str(self.user_work_link)


class Skill_set(models.Model):
    skills = models.CharField(max_length=150)

    def __str__(self):
        return self.skills


class UserRole(models.Model):
    role = models.CharField(max_length=150)

    def __str__(self):
        return self.role


class User(AbstractUser):
    profession = models.CharField(max_length=30, choices=PROFESSION_CHOISE, default="Doctor", null=True, blank=True)
    picture = models.ImageField(upload_to='user_img', default='profile/filename.jpg')
    email = models.EmailField(verbose_name='email address', max_length=150, unique=True)
    skills_id = models.ForeignKey(Skill_set, on_delete=models.CASCADE, null=True, blank=True)
    work_id = models.ForeignKey(Work_site, on_delete=models.CASCADE, null=True, blank=True)
    user_role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=150)

    REQUIRED_FIELDS = ['address', 'username']
    USERNAME_FIELD = 'email'






