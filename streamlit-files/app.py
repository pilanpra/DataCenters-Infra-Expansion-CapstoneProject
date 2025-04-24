import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


# Set page config
st.set_page_config(page_title="Data Center Cluster Predictor", layout="centered")
st.title("🏢 Data Center Cluster Predictor")
st.markdown("Use the sliders below to define your new data center and predict its cluster group.")

# Define feature inputs via slider
ENERGY = st.slider("Energy (MW)", 1.0, 150.0, 20.0)
AREA = st.slider("Area (sq.ft)", 1000, 500000, 120000)
IT_POWER = st.slider("IT Equipment Power (MW)", 0.5, 100.0, 15.0)
PUE = st.slider("Power Usage Effectiveness (PUE)", 0.0, 5.0, 0.0,1.0)
YEAR = st.slider("Year Operational", 1920, 2025, 2023)
IXP = st.slider("Internet Exchange Points", 0.0, 5.0, 0.0,1.0)

# Boolean service features
st.subheader("🛠️ Service Features")
FULL_CABINETS = st.checkbox("Full Cabinets")
PARTIAL_CABINETS = st.checkbox("Partial Cabinets")
SHARED_RACKSPACE = st.checkbox("Shared Rackspace")
CAGES = st.checkbox("Cages")
SUITES = st.checkbox("Suites")
BUILD_TO_SUIT = st.checkbox("Build To Suit")
FOOTPRINTS = st.checkbox("Footprints")
REMOTE_HANDS = st.checkbox("Remote Hands")


current_dir = os.path.dirname(os.path.abspath(__file__))

# Dynamically construct paths to the .pkl files
rf_model_path = os.path.join(current_dir, "rf_model.pkl")
scaler_path = os.path.join(current_dir, "scaler.pkl")

# Load model and scaler (you need to export these from your training code)
@st.cache_resource
def load_model():
    rf = joblib.load(rf_model_path)
    scaler = joblib.load(scaler_path)
    return rf, scaler

rf_model, scaler = load_model()

# Create input dataframe
input_df = pd.DataFrame([{
    'ENERGY': ENERGY,
    'AREA': AREA,
    'IT EQUIPMENT POWER': IT_POWER,
    'State_Aggregated_PUE': PUE,
    'FULL_CABINETS': int(FULL_CABINETS),
    'PARTIAL_CABINETS': int(PARTIAL_CABINETS),
    'SHARED_RACKSPACE': int(SHARED_RACKSPACE),
    'CAGES': int(CAGES),
    'SUITES': int(SUITES),
    'BUILD_TO_SUIT': int(BUILD_TO_SUIT),
    'FOOTPRINTS': int(FOOTPRINTS),
    'REMOTE_HANDS': int(REMOTE_HANDS),
    'YEAR_OPERATIONAL': YEAR,
    'State_Aggregated_IXP_Count': IXP
}])

# Scale and predict
scaled_input = scaler.transform(input_df)
prediction = rf_model.predict(scaled_input)

# Output
st.success(f"📌 Predicted Cluster: {prediction[0]}")
