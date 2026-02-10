from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from apps.history.models import UserActivity

from .models import Vaccination, GovtVaccination


# ---------------- USER VACCINATION DASHBOARD ----------------
@login_required 
def vaccination(request):
    user_location = request.user.location  # 👈 user’s location

    all_vaccines = Vaccination.objects.filter(
        Q(user=request.user, is_personal=True) |   # personal vaccines
        Q(
            is_approved=True,
            is_personal=False,
            location=user_location               # 👈 LOCATION FILTER
        )
    ).order_by('scheduled_date')

    govt_vaccines = GovtVaccination.objects.all()

    return render(
        request,
        'vaccination/vaccination.html',
        {
            'vaccines': all_vaccines,
            'govt_vaccines': govt_vaccines,
            'upcoming': all_vaccines.filter(status='upcoming'),
            'completed': all_vaccines.filter(status='completed'),
            'overdue': all_vaccines.filter(status='overdue'),
        }
    )

# ---------------- DOCTOR ADDS VACCINATION (PENDING) ----------------
@login_required
def add_vaccination(request):
    if request.user.role != 'DOCTOR' or not request.user.is_approved:
        messages.error(request, "You are not authorized to add vaccinations.")
        return redirect('home')

    if request.method == 'POST':
        vaccine = Vaccination.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            hospital_name=request.POST.get('hospital_name'),
            dose=request.POST.get('dose'),
            scheduled_date=request.POST.get('scheduled_date'),
            location=request.POST.get('location'),
            notes=request.POST.get('notes'),
            status='upcoming',
            is_approved=False,
            is_personal=False
        )

        UserActivity.objects.create(
            user=request.user,
            activity_type='vaccination_added',
            title='Vaccination Added',
            description=f"{vaccine.name} at {vaccine.hospital_name}",
            related_object_id=vaccine.id,
            related_app='vaccination'
        )


        messages.success(
            request,
            "Vaccination submitted. Waiting for admin approval."
        )
        return redirect('home')

    return render(request, 'vaccination/add_vaccination.html')


# ---------------- PUBLIC APPROVED VACCINATIONS ----------------

@login_required
def delete_vaccination(request, pk):
    vaccine = Vaccination.objects.get(pk=pk, user=request.user)
    vaccine.delete()
    messages.success(request, "Vaccination deleted successfully.")
    return redirect('vaccination:vaccination')

