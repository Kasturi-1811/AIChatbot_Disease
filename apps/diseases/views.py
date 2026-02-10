from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DiseaseAlert
from apps.accounts.models import CustomUser
from notifications.utils import create_notification


@login_required
def diseases(request):
    alerts = DiseaseAlert.objects.filter(
        is_active=True,
        is_approved=True
    )
    return render(request, 'diseases/diseases.html', {'alerts': alerts})


@login_required
def add_disease(request):
    if request.user.role != 'DOCTOR' or not request.user.is_approved:
        messages.error(request, "You are not authorized.")
        return redirect('diseases')

    if request.method == 'POST':
        DiseaseAlert.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            created_by=request.user,
            is_approved=False  # 🔴 PENDING
        )

        messages.success(
            request,
            "Disease alert submitted. Waiting for admin approval."
        )
        return redirect('diseases')

    return render(request, 'diseases/add_disease.html')
