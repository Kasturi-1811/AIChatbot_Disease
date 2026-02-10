from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def history(request):
    activities = request.user.activities.order_by('-created_at')
    return render(request, 'history/history.html', {
        'activities': activities
    })
