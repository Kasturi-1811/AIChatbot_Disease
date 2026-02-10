from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from apps.vaccination.models import Vaccination
from notifications.utils import create_notification


class Command(BaseCommand):
    help = "Send vaccination reminder notifications"

    def handle(self, *args, **kwargs):
        target_date = timezone.now().date() + timedelta(days=2)

        vaccines = Vaccination.objects.filter(
            scheduled_date=target_date,
            is_approved=True
        )

        for v in vaccines:
            create_notification(
                user=v.user,
                title="Vaccination Reminder ⏰",
                message=f"Your vaccination '{v.name}' is scheduled in 2 days.",
                notification_type="reminder"
            )

        self.stdout.write("Vaccination reminders sent successfully.")
