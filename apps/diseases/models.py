from django.db import models
from django.conf import settings


# apps/diseases/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.chatbot.translator import translate_text
from django.utils.translation import get_language

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
    def save(self, *args, **kwargs):

        if self.title_en and not self.title_te:
            self.title_te = translate_text(self.title_en, "Telugu")

        if self.title_en and not self.title_hi:
            self.title_hi = translate_text(self.title_en, "Hindi")

        if self.description_en and not self.description_te:
            self.description_te = translate_text(self.description_en, "Telugu")

        if self.description_en and not self.description_hi:
            self.description_hi = translate_text(self.description_en, "Hindi")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title_en} ({self.location})"
    
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

    # -----------------------------
    # 🌍 NAME
    # -----------------------------
    name_en = models.CharField(max_length=200)
    name_te = models.CharField(max_length=200, blank=True, null=True)
    name_hi = models.CharField(max_length=200, blank=True, null=True)

    alternative_names_en = models.CharField(max_length=300, blank=True,null=True)
    alternative_names_te = models.CharField(max_length=300, blank=True, null=True)
    alternative_names_hi = models.CharField(max_length=300, blank=True, null=True)

    # -----------------------------
    # 🏷 CATEGORY (Keep Single Language – It's Internal)
    # -----------------------------
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    body_system_en = models.CharField(max_length=100, blank=True,null=True   )
    body_system_te = models.CharField(max_length=100, blank=True, null=True)
    body_system_hi = models.CharField(max_length=100, blank=True, null=True)

    first_identified_year = models.CharField(max_length=50, blank=True,null=True   )

    origin_en = models.CharField(max_length=200, blank=True, null=True)
    origin_te = models.CharField(max_length=200, blank=True, null=True)
    origin_hi = models.CharField(max_length=200, blank=True, null=True)

    # -----------------------------
    # 📌 MEDICAL CONTENT
    # -----------------------------
    causes_en = models.TextField()
    causes_te = models.TextField(blank=True, null=True)
    causes_hi = models.TextField(blank=True, null=True)

    symptoms_en = models.TextField()
    symptoms_te = models.TextField(blank=True, null=True)
    symptoms_hi = models.TextField(blank=True, null=True)

    risk_factors_en = models.TextField(blank=True,null=True)
    risk_factors_te = models.TextField(blank=True, null=True)
    risk_factors_hi = models.TextField(blank=True, null=True)

    complications_en = models.TextField(blank=True,null=True)
    complications_te = models.TextField(blank=True, null=True)
    complications_hi = models.TextField(blank=True, null=True)

    transmission_type_en = models.CharField(max_length=200, blank=True, null=True)
    transmission_type_te = models.CharField(max_length=200, blank=True, null=True)
    transmission_type_hi = models.CharField(max_length=200, blank=True, null=True)

    incubation_period_en = models.CharField(max_length=100, blank=True,null=True   )
    incubation_period_te = models.CharField(max_length=100, blank=True, null=True)
    incubation_period_hi = models.CharField(max_length=100, blank=True, null=True)

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default='medium'
    )

    # -----------------------------
    # 💊 TREATMENT
    # -----------------------------
    treatment_en = models.TextField()
    treatment_te = models.TextField(blank=True, null=True)
    treatment_hi = models.TextField(blank=True, null=True)

    medicines_en = models.TextField(blank=True,null=True)
    medicines_te = models.TextField(blank=True, null=True)
    medicines_hi = models.TextField(blank=True, null=True)

    home_remedies_en = models.TextField(blank=True)
    home_remedies_te = models.TextField(blank=True, null=True)
    home_remedies_hi = models.TextField(blank=True, null=True)

    # -----------------------------
    # 🛡 PREVENTION
    # -----------------------------
    prevention_en = models.TextField(blank=True)
    prevention_te = models.TextField(blank=True, null=True)
    prevention_hi = models.TextField(blank=True, null=True)

    lifestyle_changes_en = models.TextField(blank=True,null=True)
    lifestyle_changes_te = models.TextField(blank=True, null=True)
    lifestyle_changes_hi = models.TextField(blank=True, null=True)

    # -----------------------------
    # 🏥 MEDICAL SUPPORT
    # -----------------------------
    specialist_required_en = models.CharField(max_length=200, blank=True, null=True)
    specialist_required_te = models.CharField(max_length=200, blank=True, null=True)
    specialist_required_hi = models.CharField(max_length=200, blank=True, null=True)

    hospital_phone = models.CharField(max_length=20, blank=True, null=True)

    # -----------------------------
    # 📚 EXTRA INFO
    # -----------------------------
    history_en = models.TextField(blank=True, null=True)
    history_te = models.TextField(blank=True, null=True)
    history_hi = models.TextField(blank=True, null=True)

    risk_level_en = models.CharField(max_length=100, blank=True, null=True)
    risk_level_te = models.CharField(max_length=100, blank=True, null=True)
    risk_level_hi = models.CharField(max_length=100, blank=True, null=True)

    is_vaccine_available = models.BooleanField(default=False)
    is_contagious = models.BooleanField(default=False)

    # -----------------------------
    # 🔐 ADMIN CONTROL
    # -----------------------------
    is_approved = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_diseases'
    )

    created_at = models.DateTimeField(default=timezone.now)

   


    def get_name(self):
        lang = get_language()
        if lang == "hi" and self.name_hi:
            return self.name_hi
        if lang == "te" and self.name_te:
            return self.name_te
        return self.name_en


    def get_body_system(self):
        lang = get_language()
        if lang == "hi" and self.body_system_hi:
            return self.body_system_hi
        if lang == "te" and self.body_system_te:
            return self.body_system_te
        return self.body_system_en


    def get_causes(self):
        lang = get_language()
        if lang == "hi" and self.causes_hi:
            return self.causes_hi
        if lang == "te" and self.causes_te:
            return self.causes_te
        return self.causes_en


    def get_symptoms(self):
        lang = get_language()
        if lang == "hi" and self.symptoms_hi:
            return self.symptoms_hi
        if lang == "te" and self.symptoms_te:
            return self.symptoms_te
        return self.symptoms_en


    def get_treatment(self):
        lang = get_language()
        if lang == "hi" and self.treatment_hi:
            return self.treatment_hi
        if lang == "te" and self.treatment_te:
            return self.treatment_te
        return self.treatment_en


    def get_prevention(self):
        lang = get_language()
        if lang == "hi" and self.prevention_hi:
            return self.prevention_hi
        if lang == "te" and self.prevention_te:
            return self.prevention_te
        return self.prevention_en

    def save(self, *args, **kwargs):

        fields = [
            "name",
            "body_system",
            "history",
            "origin",
            "causes",
            "symptoms",
            "risk_factors",
            "complications",
            "transmission_type",
            "incubation_period",
            "treatment",
            "medicines",
            "home_remedies",
            "prevention",
            "lifestyle_changes",
            "specialist_required",
            "risk_level",
        ]

        for field in fields:

            en = getattr(self, f"{field}_en", None)
            te = getattr(self, f"{field}_te", None)
            hi = getattr(self, f"{field}_hi", None)

            # If English exists → translate to others
            if en:
                if not te:
                    setattr(self, f"{field}_te",
                            translate_text(en, "Telugu"))
                if not hi:
                    setattr(self, f"{field}_hi",
                            translate_text(en, "Hindi"))

            # If Telugu exists but English missing
            elif te:
                if not en:
                    setattr(self, f"{field}_en",
                            translate_text(te, "English"))
                if not hi:
                    setattr(self, f"{field}_hi",
                            translate_text(te, "Hindi"))

            # If Hindi exists but English missing
            elif hi:
                if not en:
                    setattr(self, f"{field}_en",
                            translate_text(hi, "English"))
                if not te:
                    setattr(self, f"{field}_te",
                            translate_text(hi, "Telugu"))

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name_en

