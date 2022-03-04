from django.shortcuts import render, redirect, get_object_or_404
from user.models import Member
from user.forms import SignupForm, LoginForm, SettingForm, NicknameForm, NicknameFail
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
            return render(request, 'user/login.html', {"login_form": LoginForm})


def u_logout(request):
    django_logout(request)
    return redirect('home')


def u_set(request):
    setting_form = SettingForm()
    context = {
        'setting_form': setting_form
    }
    return render(request, 'user/set.html', context)


def nick_change(request):
    nickname_form = NicknameForm()
    context = {
        'nickname_form': nickname_form
    }
    return render(request, 'user/nickChange.html', context)


def nick_valid(request):
    nick = Member.objects.filter(nickname=request.POST['nickname'])
    cnt = nick.count()
    if cnt == 0:
        u = Member.objects.get(username=request.user)
        u.nickname = request.POST['nickname']
        u.save()
        return redirect('user:u_set')
    else:
        nickname_form = NicknameFail()
        context ={
            'nickname_form': nickname_form
        }
        return render(request, 'user/nickChange.html', context)
