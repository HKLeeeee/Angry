from django.shortcuts import render, redirect, get_object_or_404
from user.models import Member
from user.forms import SignupForm, LoginForm, SettingForm, NicknameForm, NicknameFail, DeleteForm, SignupFormE
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.http import HttpResponse, JsonResponse
import json


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
        if Member.objects.filter(email=request.POST['email']).count() != 0:
            signup_form_e = SignupFormE(request.POST)
            return render(request, 'user/signup.html', {"signup_form": signup_form_e})
        elif signup_form.is_valid():
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
        context = {
            'nickname_form': nickname_form
        }
        return render(request, 'user/nickChange.html', context)


def u_delete(request):
    delete_form = DeleteForm()
    context = {
        'delete_form': delete_form
    }
    return render(request, 'user/delete.html', context)


def delete_success(request):
    user = authenticate(username=request.user, password=request.POST['password'])

    if user is not None:
        user = Member.objects.filter(username=request.user)
        user.delete()
        django_logout(request)
        return render(request, 'user/deleteSuccess.html')
    else:
        return HttpResponse(user)


def aa(request):
    user = Member.objects.get(first_name='소희')
    aa = authenticate(username=user.username, password=user.password)
    django_login(request, user)
    return redirect('home')


def kakao_login(request):
    aa = request.GET['e']
    user = Member.objects.filter(email=aa)
    if user.count() == 0:
        return JsonResponse({
            'result': "false"
        }, json_dumps_params={'ensure_ascii': True})

    else:
        user = Member.objects.get(email=aa)
        django_login(request, user)
        return JsonResponse({
            'result': "success"
        }, json_dumps_params={'ensure_ascii': True})
