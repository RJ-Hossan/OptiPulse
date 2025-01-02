import streamlit as st
import importlib

# Mapping topic names to their corresponding module files
topics = {
    "Home": "frontend.home",
    # "Churn Prediction": "frontend.churn_prediction",
    "Customer Segmentation": "frontend.customer_segmentation",
    # "Lifetime Value Prediction": "frontend.lifetime_value_prediction",
    "Customer Satisfaction Analysis": "frontend.customer_satisfaction_analysis",
    # "Fault Type Prediction": "frontend.fault_type_prediction",
    # "Severity Level Prediction": "frontend.severity_level_prediction",
    "Anomaly Detection": "frontend.anomaly_detection",
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
}

# Sidebar menu
st.sidebar.title("Explore")
menu_options = list(topics.keys())
selected_topic = st.sidebar.radio("Navigate", menu_options)

# Load and run the selected module
if selected_topic:
    module_name = topics[selected_topic]
    module = importlib.import_module(module_name)
    module.run()
