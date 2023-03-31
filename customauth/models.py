from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin

# # Create your models here.
# class CustomUser(AbstractUser):
#     guild = models.TextField(max_length=1, default='')
#     motto = models.CharField(max_length=1, default='')


# class CustomUser(AbstractUser):
#     email = models.EmailField("email address", unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

