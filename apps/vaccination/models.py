from django.db import models
from django.conf import settings


class GovtVaccination(models.Model):
    AGE_GROUPS = [
        ('child', '0–5 years'),
        ('teen', '6–18 years'),
        ('adult', '19–59 years'),
        ('senior', '60+ years'),
    ]

    name = models.CharField(max_length=100)
    age_group = models.CharField(max_length=20, choices=AGE_GROUPS)
    description = models.TextField()
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
        ('overdue', 'Overdue'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=200, default="Not specified")
    dose = models.IntegerField()
    scheduled_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming'
    )

    # TYPE CONTROL
    is_personal = models.BooleanField(
        default=False,
        help_text="True if this is user's personal vaccination history"
    )

    # ADMIN APPROVAL SYSTEM
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='approved_vaccinations'
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
