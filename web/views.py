from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from web.forms import *
from web.models import *
from web.services import three_numbers, prog_day


def main_view(request):
    admin = False
    if request.user.groups.filter(name='admins'):
        admin = True
    return render(request, 'web/main.html', context={
        'admin': admin
    })


def numbers(request):
    numbers_form = ThreeNumbersForm(request.GET)
    numbers_form.is_valid()
    answer = three_numbers(numbers_form.cleaned_data)

    return render(request, 'web/numbers.html', context={
        'form': numbers_form,
        'answer': answer
    })


def reg_view(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            reg = form.cleaned_data
            return render(request, 'web/is_valid.html', context={
                'reg': reg
            })
    else:
        form = RegForm()

    return render(request, 'web/reg.html', context={
        'form': form
    })


def programmer_day(request):
    form = YearForm(request.GET)
    form.is_valid()
    day = prog_day(form.cleaned_data)

    return render(request, 'web/prog_day.html', context={
        'form': form,
        'day': day
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )

            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form,
        "is_success": is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Неправильный логин или пароль")
            else:
                login(request, user)
                return redirect("main")
    return render(request, 'web/auth.html', {
        "form": form
    })


def logout_view(request):
    logout(request)
    return redirect("auth")