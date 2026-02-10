from .models import UserActivity


def log_activity(
    user,
    activity_type,
    title,
    description="",
    related_object_id=None,
    related_app=""
):
    UserActivity.objects.create(
        user=user,
        activity_type=activity_type,
        title=title,
        description=description,
        related_object_id=related_object_id,
        related_app=related_app
    )
