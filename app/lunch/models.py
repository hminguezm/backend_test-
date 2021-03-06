import uuid
from datetime import datetime

from django.db import models


class Lunch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=100)
    create_at = models.DateField("Date", default=datetime.utcnow())

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
