# views.py
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from my_app.forms import CronJobForm, ResetForm, RegisterForm, LoginForm


def home(request):
    if request.method == "POST":
        form = CronJobForm(request.POST)

        if form.is_valid():
            form.save()

    print("home() with GET request")
    form = CronJobForm()
    return render(request, 'my_app/base.html', {'form': form})


def login(request):
    form_login = LoginForm()

    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('username')
        password = data.get('password')
        # TODO Does not work yet
        user = authenticate(username=name, password=password)
        if user is not None:
            form = CronJobForm()
            return redirect('home')
            # return render(request, 'my_app/base.html', {'form': form})
    return render(request, 'my_app/login.html', {'forms': form_login})


def register(request):
    if request.method == "POST":
        form = CronJobForm(request.POST)
        if form.ist_valid():
            user = form.save()
    register_form = RegisterForm()
    return render(request, 'my_app/register.html')


def reset(request):
    s = Test()
    # form = ResetForm()
    return render(request, 'my_app/reset.html', {'name': s})


class Test:
    first = 'have a belle'
    last = 'Tägli :)'


def email(request):
    pass
