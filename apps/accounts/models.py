from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    USER_ROLES = (
        ('USER', 'General User'),
        ('DOCTOR', 'Doctor'),
    )

    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='USER'
    )

    # Common fields
    location = models.CharField(max_length=100, blank=True, null=True)
    LANGUAGE_CHOICES = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Telugu', 'Telugu'),
   
    ]

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='English'
    )


    email_notifications = models.BooleanField(default=True)
    vaccination_reminders = models.BooleanField(default=True)

    # Doctor-specific fields
    qualification = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    hospital_name = models.CharField(max_length=150, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username
