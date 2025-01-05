import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

def run():
    # Load the best model and initialize scaler
    model = joblib.load("models/anomaly_model_oneSVM.pkl")
    scaler = StandardScaler()

    # Streamlit app title
    st.title("Anomaly Detection in Telecommunication Data")

    # Input form
    st.header("Input Data")
    latency = st.number_input("Latency (ms)", value=0.0)
    packet_loss_rate = st.number_input("Packet Loss Rate (%)", value=0.0)
    signal_strength = st.number_input("Signal Strength (dBm)", value=0.0)
    interference_level = st.number_input("Interference Level (dB)", value=0.0)
    energy_efficiency = st.number_input("Energy Efficiency (W)", value=0.0)

    # Predict button
    if st.button("Detect Anomaly"):
        # Prepare input for prediction
        input_data = np.array([[latency, packet_loss_rate, signal_strength, interference_level, energy_efficiency]])
        input_scaled = scaler.fit_transform(input_data)

        # Predict anomaly
        if hasattr(model, "predict"):
            prediction = model.predict(input_scaled)
        else:
            prediction = model.fit_predict(input_scaled)

        # Convert prediction to readable format
        anomaly_status = "Anomaly" if prediction[0] == -1 else "Normal"
        st.write(f"Prediction: **{anomaly_status}**")

if __name__ == "__main__":
    run()
