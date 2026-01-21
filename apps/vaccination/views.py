from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def vaccination(request):
    return render(request, 'vaccination/vaccination.html')

# vaccinations/views.py
from datetime import date, timedelta
from .models import Vaccination

def vaccination_notifications(user):
    today = date.today()
    reminder_day = today + timedelta(days=3)

    return Vaccination.objects.filter(
        user=user,
        scheduled_date__in=[today, reminder_day]
    )

# vaccinations/views.py
from .models import GovtVaccination

def recommended_vaccines(age):
    if age <= 5:
        group = 'child'
    elif age <= 18:
        group = 'teen'
    elif age <= 59:
        group = 'adult'
    else:
        group = 'senior'

    return GovtVaccination.objects.filter(age_group=group)
