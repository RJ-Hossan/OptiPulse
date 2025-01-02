import os
import streamlit as st
import importlib

# Mapping topic names to their corresponding module files
topics = {
    "Home": "frontend.home",
    "Anomaly Detection": "frontend.anomaly_detection",
    # "Churn Prediction": "frontend.churn_prediction",
    # "Lifetime Value Prediction": "frontend.lifetime_value_prediction",
    "Customer Satisfaction Analysis": "frontend.customer_satisfaction_analysis",
    "Customer Segmentation": "frontend.customer_segmentation",
    # "Fault Type Prediction": "frontend.fault_type_prediction",
    # "Severity Level Prediction": "frontend.severity_level_prediction",
#     "Throughput Prediction": "frontend.throughput_prediction",
#     "Latency Reduction Analysis": "frontend.latency_reduction_analysis",
#     "Energy Efficiency Modeling": "frontend.energy_efficiency_modeling",
#     "Failure Prediction": "frontend.failure_prediction",
#     "Maintenance Scheduling": "frontend.maintenance_scheduling",
#     "Revenue Forecasting": "frontend.revenue_forecasting",
#     "Contract Renewal Prediction": "frontend.contract_renewal_prediction",
#     "Service Adoption Analysis": "frontend.service_adoption_analysis",
#     "Signal Strength Analysis": "frontend.signal_strength_analysis",
#     "Interference Level Analysis": "frontend.interference_level_analysis",
#     "Packet Loss Rate Analysis": "frontend.packet_loss_rate_analysis",
    "Collaborators": "frontend.collaborators"
}

# Sidebar menu
st.sidebar.title("Explore")
menu_options = list(topics.keys())
selected_topic = st.sidebar.radio("Select your preference", menu_options)

# Load and run the selected module
if selected_topic:
    module_name = topics[selected_topic]
    module = importlib.import_module(module_name)
    module.run()

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("[Project Link](https://github.com/RJ-Hossan/OptiPulse)")

st.sidebar.markdown("Developed by Team OptiPulse_CUET")  
st.sidebar.markdown("© Telecom Data Analytics Predictor, 2024 | Team OptiPulse_CUET")