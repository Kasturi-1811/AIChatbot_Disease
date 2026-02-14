from .models import Notification


def create_notification(user, title, message, notification_type='system'):
    Notification.objects.create(
        user=user,
        title_en=title,
        message_en=message,
        notification_type=notification_type
    )
