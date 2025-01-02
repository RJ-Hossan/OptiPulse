import os
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the base directory of the project
base_dir = os.path.dirname(__file__)


# Construct the relative paths to the model files
best_model_path = os.path.join(base_dir, 'models', 'customer_satisfaction_model_LR_best.pkl')

def run():
    # Load the saved model
    model = joblib.load(best_model_path)

    # Streamlit UI
    st.title("Telecom User Satisfaction Prediction")

    # Input fields for user data using sliders for the first three columns
    Signal_Strength = st.slider('Signal Strength', min_value=-100, max_value=100, value=0)
    Latency = st.slider('Latency', min_value=0, max_value=100, value=10)
    Packet_Loss_Rate = st.slider('Packet Loss Rate', min_value=0, max_value=100, value=5)

    # Input fields for categorical features (TechSupport, DeviceProtection, StreamingTV, StreamingMovies)
    TechSupport = st.selectbox('Tech Support', ['Yes', 'No'])
    DeviceProtection = st.selectbox('Device Protection', ['Yes', 'No'])
    StreamingTV = st.selectbox('Streaming TV', ['Yes', 'No'])
    StreamingMovies = st.selectbox('Streaming Movies', ['Yes', 'No'])

    # Prepare the input data
    input_data = pd.DataFrame({
        'Signal_Strength': [Signal_Strength],
        'Latency': [Latency],
        'Packet_Loss_Rate': [Packet_Loss_Rate],
        'TechSupport': [TechSupport],
        'DeviceProtection': [DeviceProtection],
        'StreamingTV': [StreamingTV],
        'StreamingMovies': [StreamingMovies]
    })

    # Make predictions
    if st.button('Predict'):
        prediction = model.predict(input_data)
        st.write(f"Predicted User Satisfaction Index: {prediction[0]:.2f}")

        # Visualization 1: Feature Distribution (Bar Chart)
        st.subheader("Feature Distribution")
        feature_data = {
            'Tech Support': TechSupport,
            'Device Protection': DeviceProtection,
            'Streaming TV': StreamingTV,
            'Streaming Movies': StreamingMovies
        }
        
        # Convert categorical to numerical for plotting
        feature_data_numerical = {k: 1 if v == 'Yes' else 0 for k, v in feature_data.items()}
        features = list(feature_data_numerical.keys())
        values = list(feature_data_numerical.values())

        fig, ax = plt.subplots()
        ax.bar(features, values)
        ax.set_ylabel('Value')
        ax.set_title('Feature Distribution')
        st.pyplot(fig)

        # Visualization 2: Line chart for satisfaction prediction over latency
        st.subheader("Satisfaction Index Prediction Over Latency")
        latency_range = range(0, 101, 10)
        satisfaction_scores = [model.predict(pd.DataFrame({
            'Signal_Strength': [Signal_Strength],
            'Latency': [latency],
            'Packet_Loss_Rate': [Packet_Loss_Rate],
            'TechSupport': [TechSupport],
            'DeviceProtection': [DeviceProtection],
            'StreamingTV': [StreamingTV],
            'StreamingMovies': [StreamingMovies]
        })) for latency in latency_range]

        st.line_chart(pd.DataFrame({
            'Latency': latency_range,
            'Satisfaction Index': [score[0] for score in satisfaction_scores]
        }))

        # # Visualization 3: Correlation Heatmap
        # st.subheader("Correlation Heatmap of Features")
        # # Creating a dummy dataset to simulate correlation (for demonstration)
        # df = pd.DataFrame({
        #     'Signal_Strength': [Signal_Strength],
        #     'Latency': [Latency],
        #     'Packet_Loss_Rate': [Packet_Loss_Rate],
        #     'TechSupport': [1 if TechSupport == 'Yes' else 0],
        #     'DeviceProtection': [1 if DeviceProtection == 'Yes' else 0],
        #     'StreamingTV': [1 if StreamingTV == 'Yes' else 0],
        #     'StreamingMovies': [1 if StreamingMovies == 'Yes' else 0]
        # })
        # corr = df.corr()
        # fig, ax = plt.subplots(figsize=(8, 6))
        # sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        # st.pyplot(fig)

        # Visualization 4: Pie Chart for Categorical Features
        st.subheader("Pie Chart for Categorical Features")
        categories = ['TechSupport', 'DeviceProtection', 'StreamingTV', 'StreamingMovies']
        category_values = [TechSupport, DeviceProtection, StreamingTV, StreamingMovies]
        category_numerical = [1 if val == 'Yes' else 0 for val in category_values]
        category_labels = ['Yes', 'No']
        
        fig, ax = plt.subplots()
        ax.pie(category_numerical, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.set_title("Categorical Features Distribution")
        st.pyplot(fig)

        # Visualization 5: Histogram of Predictions
        st.subheader("Histogram of Predictions")
        # Generate predictions for different input values (e.g., varying Signal Strength)
        signal_strength_range = range(-100, 101, 10)
        predictions = [model.predict(pd.DataFrame({
            'Signal_Strength': [ss],
            'Latency': [Latency],
            'Packet_Loss_Rate': [Packet_Loss_Rate],
            'TechSupport': [TechSupport],
            'DeviceProtection': [DeviceProtection],
            'StreamingTV': [StreamingTV],
            'StreamingMovies': [StreamingMovies]
        })) for ss in signal_strength_range]
        
        fig, ax = plt.subplots()
        ax.hist([score[0] for score in predictions], bins=10, edgecolor='black')
        ax.set_title("Distribution of Predicted Satisfaction Index")
        ax.set_xlabel("Satisfaction Index")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

        # Visualization 6: Scatter Plot for Feature Relationships
        st.subheader("Scatter Plot for Signal Strength vs. Latency")
        fig, ax = plt.subplots()
        ax.scatter(Signal_Strength, Latency, color='blue', label="Signal Strength vs. Latency")
        ax.set_xlabel('Signal Strength')
        ax.set_ylabel('Latency')
        ax.set_title('Scatter Plot: Signal Strength vs. Latency')
        ax.legend()
        st.pyplot(fig)

# Run the application
if __name__ == "__main__":
    run()
