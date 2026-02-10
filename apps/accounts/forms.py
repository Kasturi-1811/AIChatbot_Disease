from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    ROLE_CHOICES = (
        ('USER', 'General User'),
        ('DOCTOR', 'Doctor'),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        help_text="Select Doctor only if you are a licensed medical professional."
    )

    email = forms.EmailField(
        required=True,
        help_text="e.g., nani@gmail.com (used for login & notifications)"
    )

    qualification = forms.CharField(
        required=False,
        help_text="e.g., MBBS, BDS, MD"
    )

    specialization = forms.CharField(
        required=False,
        help_text="e.g., Cardiologist, Dermatologist"
    )

    hospital_name = forms.CharField(
        required=False,
        help_text="e.g., Apollo Hospitals, Government Hospital"
    )

    license_number = forms.CharField(
        required=False,
        help_text="e.g., MCI-123456 (used for verification)"
    )

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'role',
            'location',
            'language',
            'qualification',
            'specialization',
            'hospital_name',
            'license_number',
            'password1',
            'password2',
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'e.g., nani_23'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g., Hyderabad'
            }),
            'language': forms.TextInput(attrs={
                'placeholder': 'e.g., English, Telugu'
            }),
            'qualification': forms.TextInput(attrs={
                'placeholder': 'e.g., MBBS'
            }),
            'specialization': forms.TextInput(attrs={
                'placeholder': 'e.g., General Physician'
            }),
            'hospital_name': forms.TextInput(attrs={
                'placeholder': 'e.g., Apollo Hospitals'
            }),
            'license_number': forms.TextInput(attrs={
                'placeholder': 'e.g., MCI-123456'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')

        if role == 'DOCTOR':
            required_fields = [
                'qualification',
                'specialization',
                'hospital_name',
                'license_number'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(
                        field,
                        'This field is required for doctor registration.'
                    )

        return cleaned_data


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'location',
            'language',
        )

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'e.g., nani@gmail.com'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g., Bengaluru'
            }),
            'language': forms.TextInput(attrs={
                'placeholder': 'e.g., English, Hindi'
            }),
        }
