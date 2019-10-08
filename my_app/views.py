# views.py

from django.http import HttpResponse
from django.shortcuts import render

from .forms import CronJob


def index(request):
    return HttpResponse('Hey DU ♥')


# Verweis auf Formular
def base(request):
    form = CronJob()
    return render(request, 'my_app/base.html', {'form': form})
