from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Notification


@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')
    notifications.filter(is_read=False).update(is_read=True)
    return render(
    request,
    'notifications/notification_list.html',
    {'notifications': notifications}
)
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required
@require_POST
def mark_as_read(request, pk):
    try:
        notification = Notification.objects.get(id=pk, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'success': True})
    except Notification.DoesNotExist:
        return JsonResponse({'success': False}, status=404)


@login_required
@require_POST
def mark_all_as_read(request):
    Notification.objects.filter(
        user=request.user,
        is_read=False
    ).update(is_read=True)
    return JsonResponse({'success': True})


@login_required
@require_POST
def delete_notification(request, pk):
    try:
        notification = Notification.objects.get(id=pk, user=request.user)
        notification.delete()
        return JsonResponse({'success': True})
    except Notification.DoesNotExist:
        return JsonResponse({'success': False}, status=404)

