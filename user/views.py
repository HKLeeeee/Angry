from django.shortcuts import render, redirect
from user.models import Member
from user.forms import SignupForm, LoginForm
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.http import HttpResponse


def u_login(request):
    login_form = LoginForm()

    context = {
        "login_form": login_form
    }

    return render(request, 'user/login.html', context)


def u_signup(request):
    signup_form = SignupForm()
    context = {
        "signup_form": signup_form
    }
    return render(request, 'user/signup.html', context)


def signup_success(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('user:u_login')
        else:
            return render(request, 'user/signup.html', {"signup_form": signup_form})


def login_process(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패')


def u_logout(request):
    django_logout(request)
    return redirect('home')
