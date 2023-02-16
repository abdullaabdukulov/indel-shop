# from django import forms
# from .models import Customer

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
        

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))

#     class Meta:
#         model = Customer
#         fields = ['username', 'first_name', 'last_name', 'email']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#         }
    
#     def clean_password2(self):
#         data = self.cleaned_data
#         if data['password'] != self.cleaned_data['password2']:
#             raise forms.ValidationError('Password don\'t match.')
#         return data

#     def clean_email(self):
#         data = self.cleaned_data
#         if Customer.objects.filter(email=data['email']).exists():
#             raise forms.ValidationError('Email already exists.')
#         return data

    