import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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

        # Visualize input data
        st.subheader("Input Data Visualization")
        feature_names = ["Latency", "Packet Loss Rate", "Signal Strength", "Interference Level", "Energy Efficiency"]
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(feature_names, input_data[0], color=["blue", "green", "red", "purple", "orange"])
        ax.set_title("Input Feature Values")
        ax.set_ylabel("Values")
        ax.set_xlabel("Features")
        st.pyplot(fig)

        # Highlight anomaly status
        st.subheader("Anomaly Status")
        fig2, ax2 = plt.subplots(figsize=(6, 3))
        ax2.bar(["Status"], [1 if anomaly_status == "Normal" else -1], color="green" if anomaly_status == "Normal" else "red")
        ax2.set_ylim(-1.5, 1.5)
        ax2.set_yticks([-1, 1])
        ax2.set_yticklabels(["Anomaly", "Normal"])
        ax2.set_title("Anomaly Detection Result")
        st.pyplot(fig2)

if __name__ == "__main__":
    run()
