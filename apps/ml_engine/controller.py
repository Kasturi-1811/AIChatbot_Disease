from ml_engine.ml_engine import predict_disease
from ml_engine.risk_assessment import assess_risk
from ml_engine.recommendation_engine import generate_recommendations

def run_symptom_checker(user_symptoms):
    disease = predict_disease(user_symptoms)
    risk = assess_risk(disease)
    recommendations = generate_recommendations(disease)

    return {
        "predicted_disease": disease,
        "risk_percentage": risk["percentage"],
        "risk_level": risk["level"],
        "recommendations": recommendations,
        "emergency_alert": risk["percentage"] >= 70
    }
