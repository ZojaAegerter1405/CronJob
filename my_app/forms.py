from django import forms
from django.contrib.auth.models import User

from .models import CronJob
from .models import User


class CronJobForm(forms.ModelForm):

    class Meta:
        model = CronJob
        fields = ('author', 'title', 'url')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class ResetForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)


class RegisterForm(forms.ModelForm):
    model = User
    fields = ('vorname', 'nachname', 'email', 'password')

