# Generated by Django 2.2.24 on 2021-11-28 09:57

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0002_user_model_extend"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 11, 30, 9, 57, 10, 991923, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="age",
            field=models.PositiveIntegerField(default=18, verbose_name="возраст"),
        ),
    ]
