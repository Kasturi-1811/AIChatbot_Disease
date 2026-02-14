from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from httpcore import request

from apps.history.models import UserActivity

from .models import DiseaseAlert
from apps.accounts.models import CustomUser
from notifications.utils import create_notification
from .models import Disease
from apps.chatbot.translator import translate_text

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
def add_disease(request):
    if request.user.role != 'DOCTOR' or not request.user.is_approved:
        messages.error(request, "You are not authorized.")
        return redirect('diseases')

    if request.method == 'POST':
        alert = DiseaseAlert.objects.create(
            title_en=request.POST.get('title'),
            description_en=request.POST.get('description'),
            location=request.POST.get('location'),
            created_by=request.user,
            is_approved=False
        )

        # ✅ Save Activity
        UserActivity.objects.create(
            user=request.user,
            activity_type="disease_added",
            title="Disease Alert Added",
            description=f"Added disease alert: {alert.title_en}",
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

    lang = request.LANGUAGE_CODE  # en / hi / te

    if lang == "hi":
        if not disease.name_hi:
            disease.name_hi = translate_text(disease.name_en, "Hindi")
            disease.description_hi = translate_text(disease.description_en, "Hindi")
            disease.causes_hi = translate_text(disease.causes_en, "Hindi")
            disease.symptoms_hi = translate_text(disease.symptoms_en, "Hindi")
            disease.treatment_hi = translate_text(disease.treatment_en, "Hindi")
            disease.save()

        context = {
            "name": disease.name_hi,
            "description": disease.description_hi,
            "causes": disease.causes_hi,
            "symptoms": disease.symptoms_hi,
            "treatment": disease.treatment_hi,
        }

    elif lang == "te":
        if not disease.name_te:
            disease.name_te = translate_text(disease.name_en, "Telugu")
            disease.description_te = translate_text(disease.description_en, "Telugu")
            disease.causes_te = translate_text(disease.causes_en, "Telugu")
            disease.symptoms_te = translate_text(disease.symptoms_en, "Telugu")
            disease.treatment_te = translate_text(disease.treatment_en, "Telugu")
            disease.save()

        context = {
            "name": disease.name_te,
            "description": disease.description_te,
            "causes": disease.causes_te,
            "symptoms": disease.symptoms_te,
            "treatment": disease.treatment_te,
        }

    else:
        context = {
            "name": disease.name_en,
            "description": disease.description_en,
            "causes": disease.causes_en,
            "symptoms": disease.symptoms_en,
            "treatment": disease.treatment_en,
        }

    return render(request, "diseases/detail.html", context)

@login_required
def add_library_disease(request):
    if request.user.role != 'DOCTOR' and not request.user.is_staff:
        messages.error(request, "Not authorized.")
        return redirect('diseases')

    if request.method == "POST":
        print("POST DATA:", request.POST)
        print("CATEGORY VALUE:", request.POST.get("category"))

        disease = Disease.objects.create(
            name_en=request.POST.get("name"),
            alternative_names_en=request.POST.get("alternative_names"),
            category=request.POST.get("category") or "other",

            body_system_en=request.POST.get("body_system"),
            first_identified_year=request.POST.get("first_identified_year"),
            origin_en=request.POST.get("origin"),
            causes_en=request.POST.get("causes"),
            symptoms_en=request.POST.get("symptoms"),
            risk_factors_en=request.POST.get("risk_factors"),
            complications_en=request.POST.get("complications"),
            transmission_type_en=request.POST.get("transmission_type"),
            incubation_period_en=request.POST.get("incubation_period"),
            severity=request.POST.get("severity") or "medium",

            treatment_en=request.POST.get("treatment"),
            medicines_en=request.POST.get("medicines"),
            home_remedies_en=request.POST.get("home_remedies"),
            prevention_en=request.POST.get("prevention"),
            lifestyle_changes_en=request.POST.get("lifestyle_changes"),
            specialist_required_en=request.POST.get("specialist_required"),
            hospital_phone=request.POST.get("hospital_phone"),
            is_vaccine_available=request.POST.get("is_vaccine_available") == "True",
            is_contagious=request.POST.get("is_contagious") == "True",
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
