# Generated by Django 2.2.18 on 2021-04-02 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210402_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 13, 42, 13, 376824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age_form',
            field=models.DateField(blank=True, default=datetime.date(2000, 1, 1), verbose_name='возраст'),
        ),
    ]