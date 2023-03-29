from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email_address, phone_number, password=None):
        if not email_address:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            email_address=self.normalize_email(email_address),
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, phone_number, password):
        user = self.create_user(
            email_address=email_address,
            phone_number=phone_number,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = ['email_address']

    def __str__(self):
        return self.phone_number


class Country(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Address(models.Model):
    unit_number = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250)
    region = models.CharField(max_length=250, blank=True)
    postal_code = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street_number} {self.address_line_1}, {self.city}, {self.country.name}"


class CustomAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email_address} - {self.address}"
