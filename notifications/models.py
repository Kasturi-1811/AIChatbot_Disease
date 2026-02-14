from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.chatbot.translator import translate_text
from django.utils.translation import get_language

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

    title_en = models.CharField(max_length=200, default="Notification")
    title_te = models.CharField(max_length=200, blank=True, null=True)
    title_hi = models.CharField(max_length=200, blank=True, null=True)

    message_en = models.TextField(default="")
    message_te = models.TextField(blank=True, null=True)
    message_hi = models.TextField(blank=True, null=True)


    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default='system'
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):

    # 🔹 Translate title
        if self.title_en and not self.title_te:
            self.title_te = translate_text(self.title_en, "Telugu")

        if self.title_en and not self.title_hi:
            self.title_hi = translate_text(self.title_en, "Hindi")

        # 🔹 Translate message
        if self.message_en and not self.message_te:
            self.message_te = translate_text(self.message_en, "Telugu")

        if self.message_en and not self.message_hi:
            self.message_hi = translate_text(self.message_en, "Hindi")

        super().save(*args, **kwargs)
    

    def get_title(self):
        lang = get_language()

        if lang == "hi" and self.title_hi:
            return self.title_hi
        if lang == "te" and self.title_te:
            return self.title_te

        return self.title_en


    def get_message(self):
        lang = get_language()

        if lang == "hi" and self.message_hi:
            return self.message_hi
        if lang == "te" and self.message_te:
            return self.message_te

        return self.message_en


    def __str__(self):
        return f"{self.title_en} → {self.user.username}"
