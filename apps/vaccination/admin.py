from django.contrib import admin
from django.utils import timezone
from .models import GovtVaccination, Vaccination
from notifications.utils import create_notification
from django.contrib.auth import get_user_model


@admin.register(GovtVaccination)
class GovtVaccinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_group', 'frequency')
    list_filter = ('age_group',)
    search_fields = ('name',)


@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'hospital_name',
        'location',
        'scheduled_date',
        'is_approved',
        'approved_at'
    )

    list_filter = ('is_approved', 'location')
    search_fields = ('name', 'hospital_name', 'user__username')

    actions = ['approve_vaccinations']

    def approve_vaccinations(self, request, queryset):
        User = get_user_model()

        for vaccine in queryset:
            vaccine.is_approved = True
            vaccine.approved_at = timezone.now()
            vaccine.save()

            # Get all users in the same location **except the doctor/admin**
            users_to_notify = User.objects.filter(
                location=vaccine.location
            ).exclude(id=vaccine.user.id)  # remove doctor/admin

            for user in users_to_notify:
                create_notification(
                    user=user,
                    title="New Vaccination Available 💉",
                    message=f"{vaccine.name} vaccination is now available in {vaccine.location}.",
                    notification_type="vaccination"
                )

    approve_vaccinations.short_description = "Approve selected vaccinations"
