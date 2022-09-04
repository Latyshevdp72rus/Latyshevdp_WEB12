from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from app.user.forms import RegistrationForm, LoginForm


def create_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data["password2"]
            user = User(**form.cleaned_data)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
        return redirect("stand_list_view")
    else:
        form = RegistrationForm()
    context = {
        "form": form,
        "title": "Регистрация учётной записи"
    }
    return render(request, "user/registration.html", context=context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect("stand_list_view")
            else:
                return HttpResponseRedirect("/account/invalid/")
    else:
        form = LoginForm()
    context = {
        "form": form,
        "title": "Вход на сайт"
    }
    return render(request, "user/login.html", context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("stand_list_view")
