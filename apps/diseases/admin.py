# apps/diseases/admin.py
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Disease

from .models import DiseaseAlert
from notifications.utils import create_notification


@admin.register(DiseaseAlert)
class DiseaseAlertAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'is_approved',
        'is_active',
        'created_at'
    )

    list_filter = ('location', 'is_approved', 'is_active')
    search_fields = ('title', 'description', 'location')

    actions = ['approve_disease_alerts']

    def approve_disease_alerts(self, request, queryset):
        User = get_user_model()

        for alert in queryset:
            if alert.is_approved:
                continue  # ⛔ prevent duplicate notifications

            alert.is_approved = True
            alert.approved_by = request.user
            alert.approved_at = timezone.now()
            alert.save()

            users = User.objects.filter(
                role='USER',
                location=alert.location,
                email_notifications=True
            )

            for user in users:
                create_notification(
                    user=user,
                    title=f"🚨 Disease Alert: {alert.title}",
                    message=alert.description,
                    notification_type='alert'
                )

    approve_disease_alerts.short_description = "Approve disease alerts & notify users"
@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'severity', 'is_approved', 'created_at')
    list_filter = ('category', 'severity', 'is_approved')
    search_fields = ('name', 'symptoms', 'causes')

    actions = ['approve_diseases']

    def approve_diseases(self, request, queryset):
        for disease in queryset:
            if disease.is_approved:
                continue

            disease.is_approved = True
            disease.save()

    approve_diseases.short_description = "Approve selected diseases"
