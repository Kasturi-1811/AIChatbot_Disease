from django.shortcuts import render

from notifications.models import Notification

def home(request):
    unread_count = 0

    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).count()

    return render(
        request,
        'home/home.html',
        {
            'unread_notifications': unread_count
        }
    )
