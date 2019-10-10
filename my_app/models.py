from django.contrib.auth.models import User
from django.db import models


class CronJob(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    cron_entry = models.CharField(max_length=30)
    fehlschlag_des_jobs = models.BooleanField(default=True)
    # erfolgreichem Abruf nach vorherigem Fehlschlag
    erfolg_abruf = models.BooleanField(default=True)
    # automatischer Deaktivierung wegen zu vieler Fehlschläge
    autom = models.BooleanField(default=True)
    save_answer = models.BooleanField(default=True)

    def __str__(self):
        return self.title



