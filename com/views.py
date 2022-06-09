from django.shortcuts import render, redirect
from login.models import User, Position, Company
from django.contrib import messages
from .forms import EmployeeForm
# Create your views here.


def user_list(request):
    users = User.objects.all()
    return render(request, 'userList.html', {'user': users})


def add_user(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            same_user = User.objects.filter(username=form.cleaned_data["username"])
            if same_user:
                messages.error(request, 'This account name is already exist')
                return render(request, 'addUser.html', locals())
            user = form.save()
            user.com_name = request.session['com_name']
            messages.success(request, 'account created successfully')
        return redirect("/user_list/")
    else:
        user_form = EmployeeForm()
        user_form.fields['position_name'].queryset = Position.objects.filter(company_name=request.session['user_com']).exclude(pos_name='Boss')
        return render(request, 'addUser.html', {"user_form": user_form})


def position_list(request):
    curr_com = Company.objects.filter(com_name=request.session['user_com'])
    positions = Position.objects.filter(company_name=curr_com).exclude(pos_name='Boss')
    return render(request, 'positionList.html', {'pos_list': positions})
