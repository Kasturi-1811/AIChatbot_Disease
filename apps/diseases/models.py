from django.db import models
from django.conf import settings


# apps/diseases/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone


class DiseaseAlert(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    location = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_disease_alerts'
    )

    # 🔐 ADMIN APPROVAL SYSTEM
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_disease_alerts'
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location})"
