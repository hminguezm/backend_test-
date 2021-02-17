# Generated by Django 3.1.6 on 2021-02-16 20:14

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateField(default=datetime.datetime(2021, 2, 16, 20, 14, 13, 270146), verbose_name='Date')),
            ],
        ),
    ]
