from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.history.models import UserActivity
from apps.accounts.models import CustomUser

from .models import DiseaseAlert, Disease
from notifications.models import Notification

@login_required
def diseases(request):
    alerts = DiseaseAlert.objects.filter(is_active=True, is_approved=True)
    diseases = Disease.objects.filter(is_approved=True)
    return render(request, 'diseases/diseases.html', {'alerts': alerts, 'diseases': diseases})

@login_required
def add_disease(request):
    if request.user.role != 'DOCTOR' or not request.user.is_approved:
        messages.error(request, "You are not authorized.")
        return redirect('diseases')

    if request.method == 'POST':
        alert = DiseaseAlert.objects.create(
            title_en=request.POST.get('title_en'),
            description_en=request.POST.get('description_en'),
            title_hi=request.POST.get('title_hi'),
            description_hi=request.POST.get('description_hi'),
            title_te=request.POST.get('title_te'),
            description_te=request.POST.get('description_te'),
            location=request.POST.get('location'),
            created_by=request.user,
            is_approved=False
        )

        UserActivity.objects.create(
            user=request.user,
            activity_type="disease_added",
            title="Disease Alert Added",
            description=f"Added disease alert: {alert.title_en}",
            related_object_id=alert.id,
            related_app="diseases"
        )

        messages.success(request, "Disease alert submitted. Waiting for admin approval.")
        return redirect('diseases')

    return render(request, 'diseases/add_disease.html')

@login_required
def disease_library(request):
    diseases = Disease.objects.filter(is_approved=True)
    return render(request, 'diseases/diseases.html', {'diseases': diseases})

@login_required
def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk, is_approved=True)
    return render(request, "diseases/detail.html", {"disease": disease})

@login_required
def add_library_disease(request):
    if request.user.role != 'DOCTOR' and not request.user.is_staff:
        messages.error(request, "Not authorized.")
        return redirect('diseases')

    if request.method == "POST":
        disease = Disease.objects.create(
            # ── English (required) ──
            name_en=request.POST.get("name_en"),
            causes_en=request.POST.get("causes_en"),
            symptoms_en=request.POST.get("symptoms_en"),
            treatment_en=request.POST.get("treatment_en"),
            prevention_en=request.POST.get("prevention_en"),
            home_remedies_en=request.POST.get("home_remedies_en"),

            # ── Hindi ──
            name_hi=request.POST.get("name_hi"),
            causes_hi=request.POST.get("causes_hi"),
            symptoms_hi=request.POST.get("symptoms_hi"),
            treatment_hi=request.POST.get("treatment_hi"),
            prevention_hi=request.POST.get("prevention_hi"),
            home_remedies_hi=request.POST.get("home_remedies_hi"),

            # ── Telugu ──
            name_te=request.POST.get("name_te"),
            causes_te=request.POST.get("causes_te"),
            symptoms_te=request.POST.get("symptoms_te"),
            treatment_te=request.POST.get("treatment_te"),
            prevention_te=request.POST.get("prevention_te"),
            home_remedies_te=request.POST.get("home_remedies_te"),

            # ── Common ──
            category=request.POST.get("category") or "other",
            severity=request.POST.get("severity") or "medium",

            is_approved=False,
            created_by=request.user
        )

        UserActivity.objects.create(
            user=request.user,
            activity_type="disease_added",
            title="Disease Added",
            description=f"Added disease: {disease.name_en}",
            related_object_id=disease.id,
            related_app="diseases"
        )

        messages.success(request, "Disease submitted for approval.")
        return redirect('disease_library')

    return render(request, 'diseases/add_library_disease.html')