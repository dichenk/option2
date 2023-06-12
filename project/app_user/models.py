from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=1024, verbose_name='Login', unique=True)
    password = models.CharField(max_length=1024, verbose_name='Password', unique=True)
    email = models.CharField(max_length=100, verbose_name='Email', unique=True, null=False)
    phone_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(verbose_name='date of birth', default='1971-06-28')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='user created')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='user updated')


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username