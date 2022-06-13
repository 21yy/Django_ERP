from django import forms
from django.contrib.auth import login, authenticate
from login.forms import RegisterForm
from login.models import Position


class EmployeeForm(RegisterForm):
    # address = forms.CharField(max_length=256)
    # phone_number = forms.CharField(max_length=15)
    position_name = forms.ModelChoiceField(queryset=Position.objects.all(), label='Title')

    class Meta(RegisterForm.Meta):
        fields = ["username", "position_name", "email", "password1", "password2", "gender"]


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ['pos_name', 'permissions']
        exclude = ['company_name']
