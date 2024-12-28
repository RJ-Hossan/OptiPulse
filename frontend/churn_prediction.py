import streamlit as st

def run():
    st.title("1.1 Churn Prediction")
    st.write("""
    This section is focused on churn prediction. 
    Below is a sample demonstration of the features and model implementation for churn prediction.
    """)
    
    # Example: Displaying features
    st.subheader("Features Used")
    st.write("""
    - tenure
    - Contract
    - PaperlessBilling
    - PaymentMethod
    - MonthlyCharges
    - TotalCharges
    - User_Satisfaction_Index
    """)
    
    # Add any interactive components here, such as file upload or data visualization
    st.file_uploader("Upload your dataset", type=["csv"])
    st.button("Run Churn Prediction Model")
