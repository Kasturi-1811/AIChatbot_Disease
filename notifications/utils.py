from .models import Notification


from apps.chatbot.translator import translate_text


def create_notification(user, title, message, notification_type='system'):

    # Translate using your API
    title_te = translate_text(title, "te")
    title_hi = translate_text(title, "hi")

    message_te = translate_text(message, "te")
    message_hi = translate_text(message, "hi")

    Notification.objects.create(
        user=user,
        title_en=title,
        title_te=title_te,
        title_hi=title_hi,
        message_en=message,
        message_te=message_te,
        message_hi=message_hi,
        notification_type=notification_type
    )