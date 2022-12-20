from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    image = models.ImageField(upload_to='orders/', blank=True, null=True)

    def __str__(self):
        return self.user.username