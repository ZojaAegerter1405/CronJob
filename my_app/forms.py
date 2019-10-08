from django import forms

from .models import CronJob


class CronJob(forms.ModelForm):

    class Meta:
         model = CronJob
         fields = ('title', 'url',)