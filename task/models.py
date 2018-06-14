from django.db import models
from django.utils import timezone

class Task(models.Model):
    description = models.CharField(max_length=50, blank=False)
    done = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)

