import streamlit as st

def run():
    st.title("1.2 Customer Segmentation")
    st.write("""
    This section is focused on customer segmentation using clustering techniques.
    """)
    
    # Example: Displaying features
    st.subheader("Features Used")
    st.write("""
    - MonthlyCharges
    - TotalCharges
    - InternetService
    - StreamingTV
    - StreamingMovies
    - User_Satisfaction_Index
    - tenure
    """)
    
    # Add any interactive components here
    st.file_uploader("Upload your dataset", type=["csv"])
    st.button("Run Customer Segmentation Model")
