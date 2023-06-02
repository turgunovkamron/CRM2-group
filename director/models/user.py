from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=124, null=True, blank=True)
    username = models.CharField(max_length=130, unique=True)
    surname = models.CharField(max_length=131, unique=True)
    phone = models.CharField(max_length=131, null=True, blank=True)
    password = models.CharField(max_length=1029)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    type = models.SmallIntegerField(default=0)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
