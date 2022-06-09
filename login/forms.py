from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    sex = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices=sex)

    class Meta(UserCreationForm.Meta):
        model = User
        model.password = forms.CharField(widget=forms.PasswordInput())
        fields = ["username", "email", "password1", "password2", "gender"]


class CompanyForm(RegisterForm):
    company_name = forms.CharField(max_length=256)
    address = forms.CharField(max_length=256)
    phone_number = forms.CharField(max_length=15)

    class Meta(RegisterForm.Meta):
        fields = ["company_name", "username", "email", "password1", "password2", "gender", "phone_number", "address"]


class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=128,
                               widget=forms.TextInput)
    password = forms.CharField(label="password", max_length=256,
                               widget=forms.PasswordInput)
