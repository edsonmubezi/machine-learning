import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model and encoders
model = pickle.load(open('model.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl', 'rb'))

# Page setup
st.set_page_config(page_title="Crop Yield Prediction", page_icon="🌾")

st.title("🌾 Crop Yield Prediction in Tanzania")
st.write("Enter the farming details below to predict the expected crop yield (kg per acre).")

st.markdown("---")

# User inputs
col1, col2 = st.columns(2)

with col1:
    region = st.selectbox("Region", ['Arusha', 'Dodoma', 'Iringa', 'Mbeya', 'Morogoro'])
    crop_type = st.selectbox("Crop Type", ['Beans', 'Cassava', 'Maize', 'Rice', 'Wheat'])
    soil_type = st.selectbox("Soil Type", ['Clay', 'Loam', 'Sandy'])
    irrigation = st.selectbox("Irrigation Available?", ['No', 'Yes'])

with col2:
    farm_size = st.slider("Farm Size (acres)", 0.5, 20.0, 5.0, 0.5)
    rainfall = st.slider("Rainfall (mm)", 200, 2000, 900, 50)
    temperature = st.slider("Temperature (°C)", 15, 35, 25, 1)
    fertilizer = st.slider("Fertilizer Used (kg)", 0, 200, 50, 5)

st.markdown("---")

# Predict button
if st.button("Predict Yield", type="primary"):
    # Encode categorical inputs
    region_encoded = encoders['region'].transform([region])[0]
    crop_encoded = encoders['crop_type'].transform([crop_type])[0]
    soil_encoded = encoders['soil_type'].transform([soil_type])[0]
    irrigation_val = 1 if irrigation == 'Yes' else 0

    # Create input array
    input_data = pd.DataFrame([[
        region_encoded,
        crop_encoded,
        farm_size,
        rainfall,
        temperature,
        fertilizer,
        soil_encoded,
        irrigation_val
    ]], columns=['region', 'crop_type', 'farm_size_acres', 'rainfall_mm',
                 'temperature_c', 'fertilizer_kg', 'soil_type', 'irrigation'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"**Predicted Crop Yield: {prediction:.1f} kg per acre**")

    st.markdown("---")
    st.subheader("Input Summary")
    st.write(f"- **Region:** {region}")
    st.write(f"- **Crop:** {crop_type}")
    st.write(f"- **Farm Size:** {farm_size} acres")
    st.write(f"- **Rainfall:** {rainfall} mm")
    st.write(f"- **Temperature:** {temperature} °C")
    st.write(f"- **Fertilizer:** {fertilizer} kg")
    st.write(f"- **Soil Type:** {soil_type}")
    st.write(f"- **Irrigation:** {irrigation}")

st.markdown("---")
st.caption("Machine Learning Project - Crop Yield Prediction in Tanzania")
