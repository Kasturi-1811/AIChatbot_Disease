from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import get_language

# =====================================================
# 🚨 Disease Alert Model
# =====================================================
class DiseaseAlert(models.Model):
    title_en = models.CharField(max_length=200)
    title_te = models.CharField(max_length=200, blank=True, null=True)
    title_hi = models.CharField(max_length=200, blank=True, null=True)

    description_en = models.TextField()
    description_te = models.TextField(blank=True, null=True)
    description_hi = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_disease_alerts'
    )

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
        return f"{self.title_en} ({self.location})"

    def get_field(self, field_name):
        lang = get_language()
        value = getattr(self, f"{field_name}_{lang}", None)
        if value:
            return value
        return getattr(self, f"{field_name}_en")


# =====================================================
# 📚 Disease Learning Library Model
# =====================================================
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

    # 🌍 NAME
    name_en = models.CharField(max_length=200)
    name_te = models.CharField(max_length=200, blank=True, null=True)
    name_hi = models.CharField(max_length=200, blank=True, null=True)

    alternative_names_en = models.CharField(max_length=300, blank=True, null=True)
    alternative_names_te = models.CharField(max_length=300, blank=True, null=True)
    alternative_names_hi = models.CharField(max_length=300, blank=True, null=True)

    # 🏷 CATEGORY
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    body_system_en = models.CharField(max_length=100, blank=True, null=True)
    body_system_te = models.CharField(max_length=100, blank=True, null=True)
    body_system_hi = models.CharField(max_length=100, blank=True, null=True)

    first_identified_year = models.CharField(max_length=50, blank=True, null=True)

    origin_en = models.CharField(max_length=200, blank=True, null=True)
    origin_te = models.CharField(max_length=200, blank=True, null=True)
    origin_hi = models.CharField(max_length=200, blank=True, null=True)

    # 📌 MEDICAL CONTENT
    causes_en = models.TextField()
    causes_te = models.TextField(blank=True, null=True)
    causes_hi = models.TextField(blank=True, null=True)

    symptoms_en = models.TextField()
    symptoms_te = models.TextField(blank=True, null=True)
    symptoms_hi = models.TextField(blank=True, null=True)

    risk_factors_en = models.TextField(blank=True, null=True)
    risk_factors_te = models.TextField(blank=True, null=True)
    risk_factors_hi = models.TextField(blank=True, null=True)

    complications_en = models.TextField(blank=True, null=True)
    complications_te = models.TextField(blank=True, null=True)
    complications_hi = models.TextField(blank=True, null=True)

    transmission_type_en = models.CharField(max_length=200, blank=True, null=True)
    transmission_type_te = models.CharField(max_length=200, blank=True, null=True)
    transmission_type_hi = models.CharField(max_length=200, blank=True, null=True)

    incubation_period_en = models.CharField(max_length=100, blank=True, null=True)
    incubation_period_te = models.CharField(max_length=100, blank=True, null=True)
    incubation_period_hi = models.CharField(max_length=100, blank=True, null=True)

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default='medium'
    )

    # 💊 TREATMENT
    treatment_en = models.TextField()
    treatment_te = models.TextField(blank=True, null=True)
    treatment_hi = models.TextField(blank=True, null=True)

    medicines_en = models.TextField(blank=True, null=True)
    medicines_te = models.TextField(blank=True, null=True)
    medicines_hi = models.TextField(blank=True, null=True)

    home_remedies_en = models.TextField(blank=True, null=True)
    home_remedies_te = models.TextField(blank=True, null=True)
    home_remedies_hi = models.TextField(blank=True, null=True)

    # 🛡 PREVENTION
    prevention_en = models.TextField(blank=True, null=True)
    prevention_te = models.TextField(blank=True, null=True)
    prevention_hi = models.TextField(blank=True, null=True)

    lifestyle_changes_en = models.TextField(blank=True, null=True)
    lifestyle_changes_te = models.TextField(blank=True, null=True)
    lifestyle_changes_hi = models.TextField(blank=True, null=True)

    # 🏥 MEDICAL SUPPORT
    specialist_required_en = models.CharField(max_length=200, blank=True, null=True)
    specialist_required_te = models.CharField(max_length=200, blank=True, null=True)
    specialist_required_hi = models.CharField(max_length=200, blank=True, null=True)

    hospital_phone = models.CharField(max_length=20, blank=True, null=True)

    # 📚 EXTRA
    history_en = models.TextField(blank=True, null=True)
    history_te = models.TextField(blank=True, null=True)
    history_hi = models.TextField(blank=True, null=True)

    risk_level_en = models.CharField(max_length=100, blank=True, null=True)
    risk_level_te = models.CharField(max_length=100, blank=True, null=True)
    risk_level_hi = models.CharField(max_length=100, blank=True, null=True)

    is_vaccine_available = models.BooleanField(default=False)
    is_contagious = models.BooleanField(default=False)

    # 🔐 ADMIN
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
        return self.name_en

    # 🌍 UNIVERSAL LANGUAGE GETTER
    def get_field(self, field_name):
        lang = get_language()
        value = getattr(self, f"{field_name}_{lang}", None)
        if value:
            return value
        return getattr(self, f"{field_name}_en")
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

