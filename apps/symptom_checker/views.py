import os
import joblib
from django.conf import settings
from django.shortcuts import render
from django.utils.translation import get_language
from apps.history.models import UserActivity

# --------------------------------------------------
# Load ML model safely using BASE_DIR
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

# --------------------------------------------------
# Disease Category Mapping
# --------------------------------------------------
DISEASE_CATEGORIES = {
    "Fungal infection": "skin",
    "Allergy": "skin",
    "Psoriasis": "skin",

    "Common Cold": "respiratory",
    "Pneumonia": "respiratory",
    "Tuberculosis": "respiratory",

    "Gastroenteritis": "digestive",
    "Peptic Ulcer": "digestive",

    "Diabetes": "metabolic",
    "Hypothyroidism": "metabolic",

    "Hypertension": "cardiac"
}

# --------------------------------------------------
# Category-Based Recommendations
# --------------------------------------------------
def get_recommendations_by_category(category, language="en"):

    recommendations = {

        "skin": {
            "en": {
                "care": [
                    "Keep affected area clean and dry",
                    "Avoid scratching",
                    "Use prescribed ointments"
                ],
                "lifestyle": [
                    "Wear loose cotton clothes",
                    "Maintain personal hygiene",
                    "Avoid allergens"
                ]
            },
            "te": {
                "care": [
                    "ప్రభావిత ప్రాంతాన్ని శుభ్రంగా మరియు పొడిగా ఉంచండి",
                    "గోకడం నివారించండి",
                    "వైద్యుడు సూచించిన క్రీమ్ వాడండి"
                ],
                "lifestyle": [
                    "పత్తి బట్టలు ధరించండి",
                    "వ్యక్తిగత పరిశుభ్రత పాటించండి",
                    "అలర్జీ కలిగించే పదార్థాలు దూరంగా ఉంచండి"
                ]
            },
            "hi": {
                "care": [
                    "प्रभावित क्षेत्र को साफ और सूखा रखें",
                    "खुजली से बचें",
                    "डॉक्टर द्वारा दी गई क्रीम लगाएं"
                ],
                "lifestyle": [
                    "सूती कपड़े पहनें",
                    "व्यक्तिगत स्वच्छता रखें",
                    "एलर्जी से बचें"
                ]
            }
        },

        "respiratory": {
            "en": {
                "care": [
                    "Take steam inhalation",
                    "Stay hydrated",
                    "Avoid cold exposure"
                ],
                "lifestyle": [
                    "Wear mask in polluted areas",
                    "Do breathing exercises",
                    "Get proper rest"
                ]
            },
            "te": {
                "care": [
                    "ఆవిరి పీల్చండి",
                    "తగినంత నీరు తాగండి",
                    "చల్లని వాతావరణం నివారించండి"
                ],
                "lifestyle": [
                    "మాస్క్ ధరించండి",
                    "శ్వాస వ్యాయామాలు చేయండి",
                    "తగిన విశ్రాంతి తీసుకోండి"
                ]
            },
            "hi": {
                "care": [
                    "भाप लें",
                    "पर्याप्त पानी पिएं",
                    "ठंड से बचें"
                ],
                "lifestyle": [
                    "मास्क पहनें",
                    "श्वास व्यायाम करें",
                    "पर्याप्त आराम करें"
                ]
            }
        }
    }

    if category in recommendations:
        return recommendations[category].get(language, recommendations[category]["en"])

    # Default fallback
    return {
        "care": ["Consult a doctor"],
        "lifestyle": ["Maintain a healthy lifestyle"]
    }

# --------------------------------------------------
# Main View
# --------------------------------------------------
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
        # Risk Logic
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

        # ------------------------------
        # Get Category-Based Care
        # ------------------------------
        category = DISEASE_CATEGORIES.get(prediction, "general")
        language = get_language() or "en"

        recommendation_data = get_recommendations_by_category(category, language)

        # ------------------------------
        # Final Result Dictionary
        # ------------------------------
        result = {
            "predicted_disease": prediction,
            "risk_percentage": risk_percentage,
            "risk_level": risk_level,
            "recommendations": {
                "care": recommendation_data["care"],
                "lifestyle": recommendation_data["lifestyle"],
                "warning": (
                    "Seek immediate medical attention"
                    if risk_level == "High"
                    else "Consult a doctor if symptoms persist"
                )
            },
            "emergency_alert": risk_level == "High"
        }

        # ------------------------------
        # Save User Activity
        # ------------------------------
        if request.user.is_authenticated:
            formatted_symptoms = ", ".join(
                s.replace("_", " ").title() for s in selected_symptoms
            )

            UserActivity.objects.create(
                user=request.user,
                activity_type='symptom_check',
                title='Symptom Check Completed',
                description=(
                    f"Symptoms: {formatted_symptoms}\n"
                    f"Predicted Disease: {prediction}\n"
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