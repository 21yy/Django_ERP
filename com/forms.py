from django import forms
from django.contrib.auth import login, authenticate
from login.forms import RegisterForm
from login.models import Position


class EmployeeForm(RegisterForm):
    address = forms.CharField(max_length=256)
    phone_number = forms.CharField(max_length=15)
    position_name = forms.ModelChoiceField(queryset=Position.objects.all(), required=True, label='Title')

    class Meta(RegisterForm.Meta):
        fields = ["username", "position_name", "email", "password1", "password2", "gender", "phone_number", "address"]
