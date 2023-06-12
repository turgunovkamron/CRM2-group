from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, is_superuser=False,
                    **extra_fields):
        user = self.model(email=email,
                          password=password,
                          is_staff=is_staff,
                          is_active=is_active,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        return self.create_user(email=email,
                                password=password,
                                is_superuser=True,
                                is_staff=True,
                                is_active=True,
                                **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=124, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=131, null=True, blank=True)
    password = models.CharField(max_length=1029)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    type = models.SmallIntegerField(default=0)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "join_date": self.join_date,
            "phone": self.phone,
            "type": self.type,
            "last_name": self.last_name
        }
