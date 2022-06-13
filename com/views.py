from django.shortcuts import render, redirect
from login.models import User, Position, Company
from django.contrib import messages
from .forms import EmployeeForm, PositionForm
# Create your views here.


def user_list(request):
    if request.session.get('is_login') and request.session.get('user_type', None) != 'customer':
        users = User.objects.filter(com_name=request.session['user_com'])
        return render(request, 'userList.html', {'users': users})
    else:
        return redirect('/login/')


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
            user.save()
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


def pos_list(request):
    curr_com = Company.objects.get(com_name=request.session['user_com'])
    positions = Position.objects.filter(company_name=curr_com).exclude(pos_name='Boss').values()
    return render(request, 'positionList.html', {'pos_list': positions})


def add_pos(request):
    if request.method == "POST":
        pos_form = PositionForm(request.POST)

        if pos_form.is_valid():
            same_pos = Position.objects.filter(pos_name=pos_form.cleaned_data["pos_name"])
            if same_pos:

                messages.error(request, 'This position name is already exist')
                return render(request, 'addPosition.html', locals())
            curr_com = Company.objects.get(com_name=request.session['user_com'])
            pos = pos_form.save(commit=False)
            pos.company_name = curr_com
            pos.save()
            messages.success(request, 'position created successfully')
        return redirect("/pos_list/")
    else:
        pos_form = PositionForm()
        return render(request, 'addPosition.html', {"pos_form": pos_form})


def update_pos(request):
    pos_id = request.GET.get('id')
    position = Position.objects.get(id=pos_id)
    pos_form = PositionForm(instance=position)
    if request.method == 'POST':
        update_form = PositionForm(request.POST, instance=position)
        if update_form.is_valid():
            same_user = Position.objects.filter(username=update_form.cleaned_data['pos_name'])
            if same_user:
                messages.error(request, 'This position name is already exist')
                return render(request, 'updatePosition.html', locals())
            update_form.save()

    return render(request, 'updatePosition.html', {'pos_form': pos_form})


def delete_pos(request):
    delete_id = request.GET.get('id')
    position = Position.objects.get(id=delete_id)
    if request.session['user_type'] == position.pos_name:
        messages.error(request, 'Can not delete title of yourself')
        return redirect('/pos_list')
    else:
        position.delete()
    return redirect('/pos_list')

