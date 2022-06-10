from django.shortcuts import render, redirect
from login.models import User, Position, Company
from django.contrib import messages
from .forms import EmployeeForm
# Create your views here.


def user_list(request):
    if request.session.get('is_login') and request.session.get('user_type', None) != 'customer':
        users = User.objects.filter(com_name=request.session['user_com'])
        return render(request, 'userList.html', {'users': users})
    else:
        return redirect('/login/')


def position_list(request):
    curr_com = Company.objects.filter(com_name=request.session['user_com'])
    positions = Position.objects.filter(company_name=curr_com).exclude(pos_name='Boss')
    return render(request, 'positionList.html', {'pos_list': positions})


def add_user(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            same_user = User.objects.filter(username=form.cleaned_data["username"])
            if same_user:
                messages.error(request, 'This account name is already exist')
                return render(request, 'addUser.html', locals())
            user = form.save()
            user.com_name = request.session['user_com']
            messages.success(request, 'account created successfully')
        return redirect("/user_list/")
    else:
        user_form = EmployeeForm()
        curr_com = Company.objects.get(com_name=request.session['user_com'])
        user_form.fields['position_name'].queryset = Position.objects.filter(company_name=curr_com).exclude(pos_name='Boss')
        return render(request, 'addUser.html', {"user_form": user_form})


def delete_user(request):
    delete_id = request.GET.get('id')
    if request.session['user_id'] == delete_id:
        messages.error(request, 'Can not delete yourself')
        return redirect('/user_list')
    else:
        User.objects.filter(id=delete_id).delete()
    return redirect('/user_list')


def update_user(request):
    update_id = request.GET.get('id')
    user = User.objects.get(id=update_id)
    user_form = EmployeeForm(instance=user)
    if request.method == 'POST':
        update_form = EmployeeForm(request.POST, instance=user)
        if update_form.is_valid():
            same_user = User.objects.filter(username=update_form.cleaned_data['username'])
            if same_user:
                messages.error(request, 'This account name is already exist')
                return render(request, 'updateUser.html', locals())
            update_form.save()
    curr_com = Company.objects.get(com_name=request.session['user_com'])
    user_form.fields['position_name'].queryset = Position.objects.filter(company_name=curr_com).exclude(pos_name='Boss')
    return render(request, 'updateUser.html', {'user_form': user_form})
