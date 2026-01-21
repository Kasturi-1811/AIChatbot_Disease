# vaccinations/utils.py
from datetime import date
from .models import Vaccination

def update_vaccination_status():
    today = date.today()

    for v in Vaccination.objects.all():
        if v.scheduled_date < today and v.status != 'completed':
            v.status = 'overdue'
        elif v.scheduled_date >= today and v.status != 'completed':
            v.status = 'upcoming'
        v.save()
