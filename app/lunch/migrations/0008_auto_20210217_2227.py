# Generated by Django 3.1.6 on 2021-02-17 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0007_auto_20210217_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunch',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2021, 2, 17, 22, 27, 31, 828537), verbose_name='Date'),
        ),
    ]
