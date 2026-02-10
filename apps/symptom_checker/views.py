import os
import joblib
from django.conf import settings
from django.shortcuts import render
from apps.history.models import UserActivity

# --------------------------------------------------
# Load ML model safely using BASE_DIR (IMPORTANT)
# --------------------------------------------------
MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "apps",
    "ml_engine",
    "symptom_disease_model.pkl"
)

model = joblib.load(MODEL_PATH)

# Extract ALL symptom names from trained model
ALL_SYMPTOMS = list(model.feature_names_in_)


def symptom_checker_view(request):
    result = None

    if request.method == "POST":
        selected_symptoms = request.POST.getlist("symptoms")

        # Convert symptoms to ML input format
        input_data = [
            1 if symptom in selected_symptoms else 0
            for symptom in ALL_SYMPTOMS
        ]

        prediction = model.predict([input_data])[0]

        # ------------------------------
        # Advanced AI Clinical Logic
        # ------------------------------
        symptom_count = len(selected_symptoms)

        if symptom_count >= 6:
            risk_percentage = 85
        elif symptom_count >= 3:
            risk_percentage = 60
        else:
            risk_percentage = 35

        if risk_percentage >= 70:
            risk_level = "High"
        elif risk_percentage >= 40:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        result = {
            "predicted_disease": prediction,
            "risk_percentage": risk_percentage,
            "risk_level": risk_level,
            "recommendations": {
                "care": [
                    "Keep affected area clean and dry",
                    "Avoid self-medication",
                    "Follow proper hygiene"
                ],
                "lifestyle": [
                    "Drink sufficient water",
                    "Eat nutritious food",
                    "Get adequate rest"
                ],
                "warning": (
                    "Seek immediate medical attention"
                    if risk_level == "High"
                    else "Consult a doctor if symptoms persist"
                )
            },
            "emergency_alert": risk_level == "High"
        }
        if request.user.is_authenticated:
            UserActivity.objects.create(
                user=request.user,
                activity_type='chatbot_chat',
                title='Symptom Check Completed',
                description=(
                    f"Predicted Disease: {prediction}, "
                    f"Risk Level: {risk_level} ({risk_percentage}%)"
                ),
                related_app='symptom_checker'
            )


    return render(
        request,
        "symptom_checker/symptom_checker.html",
        {
            "symptoms": ALL_SYMPTOMS,
            "result": result
        }
    )
