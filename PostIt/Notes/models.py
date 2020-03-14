from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Notes(models.Model):
    task = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task