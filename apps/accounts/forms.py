from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=100, required=False)
    language = forms.CharField(max_length=50, required=False)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'location',
            'language',
            'password1',
            'password2'
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'location',
            'language',
        )
