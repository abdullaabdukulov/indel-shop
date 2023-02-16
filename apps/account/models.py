# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField



# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank = True)
#     adress = models.CharField(max_length=400, blank=True, null=True)
#     phone_number = PhoneNumberField(blank=True, null=True, unique=True)
#     image = models.ImageField(upload_to='users/', blank=True, null=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#     class Meta:
#         verbose_name = "Profile"
#         verbose_name_plural = 'Profiles'
        

