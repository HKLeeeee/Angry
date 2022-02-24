from django.shortcuts import render, redirect
from user.models import Member
from user.forms import SigninForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout, authenticate
from django.http import HttpResponse


def u_login(request):
    login_form = LoginForm()

    context = {
        "login_form": login_form
    }

    return render(request, 'user/login.html', context)


def u_signin(request):
    signin_form = SigninForm()
    context = {
        "signin_form": signin_form
    }
    return render(request, 'user/signin.html', context)


def signin_success(request):
    return redirect('home')


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
