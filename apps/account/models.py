from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email_address, phone_number, password=None, **extra_fields):
        if not email_address:
            raise ValueError('The Email Address field must be set')
        if not phone_number:
            raise ValueError('The Phone Number field must be set')

        email_address = self.normalize_email(email_address)
        user = self.model(email_address=email_address, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email_address, phone_number, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email_address']

    def __str__(self):
        return self.email_address
