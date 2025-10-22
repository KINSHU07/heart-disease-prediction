import streamlit as st
import numpy as np
import pickle
import joblib  # or import pickle if you used pickle

# Load your trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)  # Replace with your model filename

st.title("💓 Heart Disease Prediction ")

st.write("""
This app predicts the likelihood of a person having **heart disease** based on several health parameters.
Please fill out the form below:
""")

# User inputs
age = st.slider("Age", 1, 120, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.slider("Max Heart Rate Achieved (thalach)", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.slider("ST Depression Induced by Exercise (oldpeak)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [0, 1, 2])

ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Convert sex to binary
sex_bin = 1 if sex == "Male" else 0

# Prepare input array
input_features = np.array([[age, sex_bin, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])

# Make prediction
if st.button("🔍 Predict"):
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ This person is likely **prone to heart disease**.\n\n**Risk Probability: {probability:.2f}**")
    else:
        st.success(f"✅ This person is **not prone to heart disease**.\n\n**Risk Probability: {probability:.2f}**")
