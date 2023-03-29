from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import CustomUser, Address, CustomAddress


class CustomUserCreationForm(UserCreationForm):
    email_address = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email_address', 'phone_number', 'password1', 'password2')
        username = None


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class CustomAddressForm(ModelForm):
    class Meta:
        model = CustomAddress
        fields = ('address', 'is_default')