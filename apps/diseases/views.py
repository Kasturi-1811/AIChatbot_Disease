from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.history.models import UserActivity

from .models import DiseaseAlert
from apps.accounts.models import CustomUser
from notifications.utils import create_notification
from .models import Disease


@login_required
def diseases(request):
    alerts = DiseaseAlert.objects.filter(
        is_active=True,
        is_approved=True
    )

    diseases = Disease.objects.filter(is_approved=True)
  
    return render(request, 'diseases/diseases.html', {
        'alerts': alerts,
        'diseases': diseases   # 👈 ADD THIS
    })

@login_required
@login_required
def add_disease(request):
    if request.user.role != 'DOCTOR' or not request.user.is_approved:
        messages.error(request, "You are not authorized.")
        return redirect('diseases')

    if request.method == 'POST':
        alert = DiseaseAlert.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            created_by=request.user,
            is_approved=False
        )

        # ✅ Save Activity
        UserActivity.objects.create(
    user=request.user,
    activity_type="disease_added",
    title="Disease Alert Added",
    description=f"Added disease alert: {alert.title}",
    related_object_id=alert.id,
    related_app="diseases"
)


        messages.success(
            request,
            "Disease alert submitted. Waiting for admin approval."
        )
        return redirect('diseases')

    return render(request, 'diseases/add_disease.html')

def disease_library(request):
    diseases = Disease.objects.all()
    print(diseases)
    return render(request, 'diseases/diseases.html', {
        'diseases': diseases
    })

def disease_detail(request, pk):
    disease = Disease.objects.get(pk=pk, is_approved=True)
    return render(request, 'diseases/detail.html', {
        'disease': disease
    })
@login_required
def add_library_disease(request):
    if request.user.role != 'DOCTOR' and not request.user.is_staff:
        messages.error(request, "Not authorized.")
        return redirect('diseases')

    if request.method == "POST":

        disease = Disease.objects.create(
            name=request.POST.get("name"),
            alternative_names=request.POST.get("alternative_names"),
            category=request.POST.get("category"),
            body_system=request.POST.get("body_system"),
            first_identified_year=request.POST.get("first_identified_year"),
            origin=request.POST.get("origin"),
            causes=request.POST.get("causes"),
            symptoms=request.POST.get("symptoms"),
            risk_factors=request.POST.get("risk_factors"),
            complications=request.POST.get("complications"),
            transmission_type=request.POST.get("transmission_type"),
            incubation_period=request.POST.get("incubation_period"),
            severity=request.POST.get("severity"),
            treatment=request.POST.get("treatment"),
            medicines=request.POST.get("medicines"),
            home_remedies=request.POST.get("home_remedies"),
            prevention=request.POST.get("prevention"),
            lifestyle_changes=request.POST.get("lifestyle_changes"),
            specialist_required=request.POST.get("specialist_required"),
            hospital_phone=request.POST.get("hospital_phone"),
            is_vaccine_available=request.POST.get("is_vaccine_available") == "True",
            is_contagious=request.POST.get("is_contagious") == "True",
            is_approved=False,
            created_by=request.user
        )

        # ✅ Save Activity INSIDE POST
        UserActivity.objects.create(
    user=request.user,
    activity_type="disease_added",
    title="Disease Added",
    description=f"Added disease: {disease.name}",
    related_object_id=disease.id,
    related_app="diseases"
)


        messages.success(request, "Disease submitted for approval.")
        return redirect('disease_library')

    return render(request, 'diseases/add_library_disease.html')
