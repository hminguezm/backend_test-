# Generated by Django 3.1.6 on 2021-02-17 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0006_auto_20210217_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunch',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2021, 2, 17, 22, 16, 45, 975598), verbose_name='Date'),
        ),
    ]
