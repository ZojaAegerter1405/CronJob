from django.db import models


class CronJob(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    save_answer = models.BooleanField(default=True)
