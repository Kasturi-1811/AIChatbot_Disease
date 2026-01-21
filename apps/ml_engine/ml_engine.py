import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "symptom_disease_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_disease(user_symptoms):
    symptoms = model.feature_names_in_
    input_data = [1 if s in user_symptoms else 0 for s in symptoms]
    return model.predict([input_data])[0]
