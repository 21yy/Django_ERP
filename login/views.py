from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Position, Company, User
from .forms import RegisterForm, UserForm, CompanyForm


# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        name = login_form.data['username']
        password = login_form.data['password']
        message = ''
        if login_form.is_valid():
            name = name.strip()
            try:
                user = User.objects.get(username=name)
                if check_password(password, user.password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    request.session['user_type'] = user.type
                    request.session['user_com'] = user.com_name
                    return redirect('/')
                else:
                    message = 'username or password is incorrect'
            except:
                message = 'username or password is incorrect'
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())


def register_user(request):
    if request.method == "POST":
        customer = Position.objects.get(pos_name="customer", company_name="admin")
        # if not customer:
        #     customer = Position.objects.create(pos_name="customer", company_name="admin")
        form = RegisterForm(request.POST)
        if form.is_valid():
            same_user = User.objects.filter(username=form.cleaned_data["username"])
            if same_user:
                messages.error(request, 'This account name is already exist')
                return render(request, 'register.html', locals())
            user = form.save()
            user.type = customer
            messages.success(request, 'account created successfully')
        return redirect("/login/")
    else:
        user_form = RegisterForm()
        com_form = CompanyForm()
        return render(request, 'register.html', {"user_form": user_form, "com_form": com_form})


def register_company(request):
    if request.method == "POST":
        com_form = CompanyForm(request.POST)
        user_form = RegisterForm(request.POST)
        message = ''
        if com_form.is_valid() and user_form.is_valid():
            same_com = Company.objects.filter(com_name=com_form.cleaned_data['company_name'])
            same_user = User.objects.filter(username=user_form.cleaned_data['username'])
            if same_com:
                message = 'This company registered already'
            elif same_user:
                message = 'The same account name exists'
            else:
                new_com = Company.objects.create(com_name=com_form.cleaned_data['company_name'],
                                                 address=com_form.cleaned_data['address'],
                                                 phone_number=com_form.cleaned_data['phone_number'])
                position = Position.objects.create(pos_name="Boss", company_name=new_com,  permissions=1)
                user = user_form.save(commit=False)
                user.type = position
                user.com_name = new_com
                user.save()
                messages.success(request, 'Account registered successfully')
            return redirect("/login/")
        user_form = RegisterForm()
        return render(request, 'register.html', locals())
    else:
        user_form = RegisterForm()
        com_form = CompanyForm()
        return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/")
    request.session.flush()
    return render(request, 'index.html')
