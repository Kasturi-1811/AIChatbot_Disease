from django.db import models
from django.conf import settings
from django.utils import timezone


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('vaccination', 'Vaccination'),
        ('reminder', 'Reminder'),
        ('alert', 'Disease Alert'),
        ('system', 'System'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    title = models.CharField(
        max_length=200,
        default="Notification"   # ✅ ADD DEFAULT
    )

    message = models.TextField(
        default=""               # ✅ ADD DEFAULT
    )

    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default='system'
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} → {self.user.username}"
