from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'role',
        'is_approved',
        'is_staff',
        'is_active',
        'date_joined'
    )

    list_filter = (
        'role',
        'is_approved',
        'is_staff',
        'is_active',
        'date_joined'
    )

    search_fields = (
        'username',
        'email',
        'license_number',
        'hospital_name',
        'specialization'
    )

    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {
            'fields': (
                'role',
                'is_approved',
                'location',
                'language',
            )
        }),
        ('Doctor Information', {
            'fields': (
                'qualification',
                'specialization',
                'hospital_name',
                'license_number',
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Information', {
            'fields': (
                'role',
                'location',
            )
        }),
    )

    # Make is_approved editable directly in list view
    list_editable = ('is_approved',)
