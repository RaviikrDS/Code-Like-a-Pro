import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

st.title("Insurance Claim Cost Predictor")

payload = {
    "age": st.number_input("Age", 18, 100),
    "annual_income": st.number_input("Annual Income", 1000),
    "vehicle_age": st.number_input("Vehicle Age", 0),
    "past_claims": st.number_input("Past Claims", 0),
    "accident_severity": st.slider("Accident Severity", 1, 5),
    "policy_tenure": st.number_input("Policy Tenure", 1),
}

if st.button("Predict"):
    response = requests.post(API_URL, json=payload)
    result = response.json()
    st.success(f"Estimated Claim Amount: ₹{result['estimated_claim_amount']:.2f}")
