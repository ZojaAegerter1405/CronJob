# Generated by Django 2.2.6 on 2019-10-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronjob',
            name='save_answer',
            field=models.BooleanField(default=True),
        ),
    ]
