from django.db import models
from django.conf import settings


# apps/diseases/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone


class DiseaseAlert(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    location = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_disease_alerts'
    )

    # 🔐 ADMIN APPROVAL SYSTEM
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_disease_alerts'
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location})"
    
    # ---------------------------------------------
# 📚 Disease Learning Library Model
# ---------------------------------------------

class Disease(models.Model):

    CATEGORY_CHOICES = (
        ('viral', 'Viral'),
        ('bacterial', 'Bacterial'),
        ('fungal', 'Fungal'),
        ('genetic', 'Genetic'),
        ('chronic', 'Chronic'),
        ('skin', 'Skin'),
        ('other', 'Other'),
    )

    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    name = models.CharField(max_length=200)
    alternative_names = models.CharField(max_length=300, blank=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    body_system = models.CharField(max_length=100)

    first_identified_year = models.CharField(max_length=50, blank=True)
    origin = models.CharField(max_length=200, blank=True)

    causes = models.TextField()
    symptoms = models.TextField()
    risk_factors = models.TextField(blank=True)
    complications = models.TextField(blank=True)

    transmission_type = models.CharField(max_length=200, blank=True)
    incubation_period = models.CharField(max_length=100, blank=True)

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default='medium'
    )

    treatment = models.TextField()
    medicines = models.TextField(blank=True)
    home_remedies = models.TextField(blank=True)

    prevention = models.TextField(blank=True)
    lifestyle_changes = models.TextField(blank=True)

    specialist_required = models.CharField(
    max_length=200,
    blank=True,
    null=True
)
    hospital_phone = models.CharField(max_length=20, blank=True, null=True)



    is_vaccine_available = models.BooleanField(default=False)
    history = models.TextField(blank=True, null=True)
    risk_level = models.CharField(max_length=100, blank=True, null=True)
    is_contagious = models.BooleanField(default=False)

        # Admin approval (optional safety)
    is_approved = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_diseases'
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

