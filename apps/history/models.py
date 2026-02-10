from django.db import models
from django.conf import settings
from django.utils import timezone


class UserActivity(models.Model):

    ACTIVITY_TYPES = (
        ('disease_added', 'Disease Added'),
        ('vaccination_added', 'Vaccination Added'),
        ('vaccination_completed', 'Vaccination Completed'),
        ('quiz_attempted', 'Quiz Attempted'),
        ('quiz_created', 'Quiz Created'),
        ('chatbot_chat', 'Chatbot Interaction'),
        ('personal_vaccination', 'Personal Vaccination Added'),
        ('notification_received', 'Notification Received'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    activity_type = models.CharField(
        max_length=50,
        choices=ACTIVITY_TYPES
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    related_object_id = models.PositiveIntegerField(null=True, blank=True)
    related_app = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"
