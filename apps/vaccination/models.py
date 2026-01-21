# vaccinations/models.py
from django.db import models
from django.conf import settings

# vaccinations/models.py
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
    frequency = models.CharField(max_length=100)  # once, yearly, booster


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
    dose = models.IntegerField()
    scheduled_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
