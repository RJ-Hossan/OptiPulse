import os
import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run():
    st.title("Customer Segmentation")

    st.header("Input Customer Attributes")

    # Input fields for customer attributes
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=0.01)
    total_charges = st.number_input("Total Charges", min_value=0.0, step=0.01)
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No"])
    user_satisfaction_index = st.slider("User Satisfaction Index", min_value=1, max_value=10, step=1)
    tenure = st.number_input("Tenure (Months)", min_value=0, step=1)

    # Convert inputs to a DataFrame
    input_data = pd.DataFrame({
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "InternetService": [internet_service],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "User_Satisfaction_Index": [user_satisfaction_index],
        "tenure": [tenure]
    })

    # Preprocess the input data
    def preprocess_data(data):
        # Encoding categorical features
        data["InternetService"] = data["InternetService"].map({"DSL": 0, "Fiber optic": 1, "No": 2})
        data["StreamingTV"] = data["StreamingTV"].map({"Yes": 1, "No": 0})
        data["StreamingMovies"] = data["StreamingMovies"].map({"Yes": 1, "No": 0})

        # Standardize numerical features
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        return scaled_data

    if st.button("Predict Cluster"):
        processed_data = preprocess_data(input_data)

        # Get the base directory of the project
        base_dir = os.path.dirname(__file__)

        # Construct the relative paths to the model files
        model_path = os.path.join(base_dir, '../models', 'kmeans_model.pkl')

        # Load the model and make predictions
        @st.cache_resource
        def load_model():
            return joblib.load(model_path)

        model = load_model()
        cluster_label = model.predict(processed_data)[0]

        # Display the cluster label
        st.subheader("Customer Segmentation Result")
        st.write(f"This customer belongs to Cluster {cluster_label}.")
        
if __name__ == "__main__":
    run()
