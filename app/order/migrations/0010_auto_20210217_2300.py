# Generated by Django 3.1.6 on 2021-02-17 23:00

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20210217_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('applicant_name', models.CharField(max_length=100)),
                ('meal', models.CharField(choices=[], max_length=2)),
                ('comment', models.TextField(max_length=100)),
                ('create_at', models.DateField(default=datetime.datetime(2021, 2, 17, 23, 0, 1, 57337), verbose_name='Date')),
            ],
        ),
        migrations.DeleteModel(
            name='Lunch',
        ),
    ]