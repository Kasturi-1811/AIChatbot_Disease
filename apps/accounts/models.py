from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=20, default='en')

    email_notifications = models.BooleanField(default=True)
    vaccination_reminders = models.BooleanField(default=True)

    def __str__(self):
        return self.username
