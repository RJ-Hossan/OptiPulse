# OptiPulse
Comprehensive Machine Learning Solutions for Customer Analytics, Network Optimization, Predictive Maintenance, and Business Intelligence.

**Clone the repo in your local machine**
`git clone https://github.com/RJ-Hossan/OptiPulse.git`

Then select the folder and write following command in respective folder

`streamlit run app.py`



**Telecom Anomaly Detection Documentation**

This documentation explains each step of the anomaly detection process, covering data preparation, processing, model training, and visualization.


![image](https://github.com/user-attachments/assets/aaa2eda4-cd43-4f8e-8a55-2f4ce6360ef4)
![image](https://github.com/user-attachments/assets/81dd13c7-e055-46d8-acb2-799276283a9b)


---

### 1. **Importing Necessary Libraries**

```python
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
```

- **os**: Used to navigate directories.
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib** and **seaborn**: For data visualization.
- **scikit-learn**: For preprocessing and implementing anomaly detection algorithms.

---

### 2. **Setting the Working Directory**

```python
base_dir = r"C:\Users\ASUS\Downloads\Telecom Anomaly Detection"
os.chdir(base_dir)
```

- Changes the current working directory to the location where the data and scripts are stored.
- Ensures seamless loading and saving of files within the same directory.

---

### 3. **Loading the Dataset**

```python
data_file = 'telecom_anomaly.csv'
data = pd.read_csv(data_file)
```

- Reads the dataset `telecom_anomaly.csv` into a DataFrame for further processing.
- Assumes the file contains columns relevant to the problem domain, such as network parameters.


![Glimpse](https://github.com/user-attachments/assets/295c6302-a26a-40dc-abd0-f3022d2732e2)


---

### 4. **Handling Missing Values**

```python
if data.isnull().sum().sum() > 0:
    print("Filling missing values with column means...")
    data.fillna(data.mean(), inplace=True)
```

- Checks for missing values in the dataset.
- If missing values are found, fills them with the mean of their respective columns to maintain consistency.
- Prints a message for transparency.

---

### 5. **Selecting Features for Anomaly Detection**

```python
features = ['Latency', 'Packet_Loss_Rate', 'Signal_Strength', 'Interference_Level', 'Energy_Efficiency']
X = data[features]
```

- Specifies the features (columns) relevant for detecting anomalies.
- Extracts these features into a new DataFrame `X` for preprocessing and model training.

---

### 6. **Standardizing the Features**

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

- Standardizes the features to have zero mean and unit variance.
- Standardization ensures better performance for distance-based algorithms like Isolation Forest and One-Class SVM.

---

### 7. **Anomaly Detection Using Isolation Forest**

```python
iso_forest = IsolationForest(contamination=0.1, random_state=42)
y_pred_iso = iso_forest.fit_predict(X_scaled)
data['Anomaly_Isolation_Forest'] = y_pred_iso
```

- **Isolation Forest**:
  - A tree-based algorithm that isolates anomalies by randomly splitting data.
  - `contamination=0.1`: Assumes 10% of the data are anomalies.
  - `random_state=42`: Ensures reproducibility.
- Adds a new column `Anomaly_Isolation_Forest` to the DataFrame with anomaly labels (`1` for normal, `-1` for anomaly).





---

### 8. **Saving the Results**

```python
output_file = 'telecom_anomaly_with_labels.csv'
data.to_csv(output_file, index=False)
print(f"Processed data with anomaly labels saved to {output_file}.")
```

- Saves the updated DataFrame, including anomaly labels, to a new CSV file.
- Prints a confirmation message with the file name.

---

### 9. **Visualization for Isolation Forest**

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=data['Latency'],
    y=data['Packet_Loss_Rate'],
    hue=data['Anomaly_Isolation_Forest'],
    palette={1: 'blue', -1: 'red'}
)
plt.title('Anomaly Detection using Isolation Forest')
plt.xlabel('Latency')
plt.ylabel('Packet Loss Rate')
plot_file = 'anomaly_detection_plot.png'
plt.savefig(plot_file)
print(f"Anomaly detection plot saved to {plot_file}.")
plt.show()
```

- Creates a scatter plot of `Latency` vs. `Packet Loss Rate`, highlighting anomalies in red and normal points in blue.
- Saves the plot as `anomaly_detection_plot.png` for further analysis.

![anomaly_detection_isolation_forest](https://github.com/user-attachments/assets/0cbdb49d-46b5-4899-a5c1-2d13a5d0de61)

---

### 10. **Anomaly Detection Using Local Outlier Factor (LOF)**

```python
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred_lof = lof.fit_predict(X_scaled)
data['Anomaly_LOF'] = y_pred_lof
```

- **Local Outlier Factor**:
  - Identifies anomalies by measuring the local density deviation of data points.
  - `n_neighbors=20`: Considers 20 nearest neighbors.
  - `contamination=0.1`: Assumes 10% of the data are anomalies.
- Adds a new column `Anomaly_LOF` with anomaly labels.

---

### 11. **Visualization for LOF**

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Latency'], y=data['Signal_Strength'], hue=data['Anomaly_LOF'], palette={1: 'blue', -1: 'red'})
plt.title('Anomaly Detection using LOF')
plt.show()
```

- Visualizes anomalies detected by LOF using `Latency` and `Signal Strength` as axes.
- Highlights anomalies in red and normal points in blue.

![anomaly_detection_lof](https://github.com/user-attachments/assets/0b2fe5f3-4d9d-45c2-a714-c461cda15d68)



---

### 12. **Anomaly Detection Using One-Class SVM**

```python
svm = OneClassSVM(nu=0.1, kernel='rbf', gamma='scale')
y_pred_svm = svm.fit_predict(X_scaled)
data['Anomaly_SVM'] = y_pred_svm
```

- **One-Class SVM**:
  - A classification algorithm that separates normal data from outliers.
  - `nu=0.1`: Upper bound on the fraction of training errors (assumes 10% anomalies).
  - `kernel='rbf'`: Uses a radial basis function kernel.
- Adds a new column `Anomaly_SVM` with anomaly labels.



![anomaly_detection_svm](https://github.com/user-attachments/assets/a5f66795-5096-4643-be12-ca37ac241270)


---

### 13. **Visualization for One-Class SVM**

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Energy_Efficiency'], y=data['Throughput'], hue=data['Anomaly_SVM'], palette={1: 'blue', -1: 'red'})
plt.title('Anomaly Detection using One-Class SVM')
plt.show()
```

- Visualizes anomalies detected by One-Class SVM using `Energy Efficiency` and `Throughput` as axes.

---

### 14. **Pair Plots for Comparison**

```python
sns.pairplot(data, hue="Anomaly_Isolation_Forest", vars=features, palette={1: 'blue', -1: 'red'})
plt.suptitle('Pair Plot for Isolation Forest Anomalies', y=1.02)
plt.show()

sns.pairplot(data, hue="Anomaly_LOF", vars=features, palette={1: 'blue', -1: 'red'})
plt.suptitle('Pair Plot for LOF Anomalies', y=1.02)
plt.show()

sns.pairplot(data, hue="Anomaly_SVM", vars=features, palette={1: 'blue', -1: 'red'})
plt.suptitle('Pair Plot for One-Class SVM Anomalies', y=1.02)
plt.show()
```

- Creates pair plots to compare the anomalies detected by each method across all features.
- Highlights anomalies in red and normal points in blue for visual analysis of relationships.

  ![pairplot_isolation_forest](https://github.com/user-attachments/assets/c54b78d3-c5a8-4ab9-8a9b-c121ca05a31f)


---

![pairplot_svm](https://github.com/user-attachments/assets/19b68e21-ce36-4494-84cf-5df3f12cfaf2)
![pairplot_lof](https://github.com/user-attachments/assets/673b9804-6fba-438f-87ae-160173ec1806)





### Task 2: Customer Satisfaction Analysis Documentation

#### Overview
This task focuses on performing regression analysis to quantify factors influencing customer satisfaction. By understanding what drives satisfaction and dissatisfaction, Robi Axiata can implement targeted strategies to enhance customer experiences, reduce churn, and drive business growth.

![image](https://github.com/user-attachments/assets/11116f6c-a648-4b3c-a63b-c22b42e4b4be)

#### Objectives
- Identify key factors affecting customer satisfaction.
- Uncover drivers of dissatisfaction to mitigate negative experiences.
- Enable data-driven decision-making for service improvement.

#### Dataset
- **Source**: Network parameters from Robi Axiata's systems.
- **Features**: 35 features including service usage data, customer interactions, and feedback scores.
- **Size**: 402,547 data points.


#### Methodology
1. **Data Preprocessing**:
   - Handle missing values and outliers.
   - Normalize or standardize numerical data to ensure model accuracy.

2. **Feature Selection**:
   - Utilize correlation analysis to identify significant predictors of satisfaction.

3. **Model Development**:
   - **Linear Regression**: Establishes a baseline for understanding linear relationships.
   - **Decision Tree**: Captures non-linear patterns and interactions between variables.
   - **Random Forest**: Enhances prediction accuracy through ensemble learning, reducing overfitting.
   - **Gradient Boosting**: Focuses on correcting the errors of prior models, continuously improving performance.

4. **Evaluation**:
   - Use MAE (Mean Absolute Error), MSE (Mean Squared Error), and R2-score to assess model performance.
   - Visualize results to interpret model effectiveness in predicting customer satisfaction.

5. **Implementation**:
   - Deploy the best-performing model to predict satisfaction levels for new customer data.
   - Continuously update the model with new data to improve accuracy.


![image](https://github.com/user-attachments/assets/9617533e-6585-4787-b3ee-24696cd1dc90)
![Best Model on test set](https://github.com/user-attachments/assets/085ca57f-0104-4805-9670-750a77047913)

#### Visualization
- Distribution of customer satisfaction indices.
- Pair plots of selected features against satisfaction scores.
- Performance metrics visualization on validation and test datasets.

![image](https://github.com/user-attachments/assets/aab24ab6-e3c5-4d1c-a75a-e18d4a555513)
![image](https://github.com/user-attachments/assets/b5e356b6-da2e-4d72-8b13-7b2f751bc3ff)

### Task 3: Customer Segmentation Documentation

#### Overview
Customer segmentation aims to categorize customers into distinct groups based on shared characteristics. This strategic approach helps in personalizing marketing efforts, optimizing resource allocation, and enhancing overall customer satisfaction.

![image](https://github.com/user-attachments/assets/e619452b-1d6f-4ac6-9bda-12575322e249)


#### Objectives
- Divide customers into behaviorally and demographically similar groups.
- Tailor marketing and service approaches to meet the specific needs of each segment.

#### Dataset
- **Source**: Network parameters and customer demographic data from Robi Axiata.
- **Features**: Usage patterns, payment history, service options, and customer demographics.
- **Preprocessing Steps**:
  - Handling missing values.
  - Encoding categorical features.
  - Scaling data to prepare for clustering.

#### Methodology
1. **Exploratory Data Analysis**:
   - Understand the underlying structure and relationships within the data.
   - Identify anomalies or distinctive patterns across customer behaviors.

2. **Clustering**:
   - **K-Means Clustering**: Efficiently partitions customers into k distinct clusters based on feature similarity.
   - **Silhouette Analysis**: Validates the appropriateness of the number of clusters.
   - **PCA (Principal Component Analysis)**: Reduces dimensionality while preserving the most important variance features.

3. **Evaluation**:
   - Assess clusters' quality and distinctiveness using silhouette scores.
   - Perform cluster profiling to understand the characteristics of each group.

4. **Implementation**:
   - Apply clustering insights to customize marketing strategies and service offerings.
   - Monitor and adjust the segmentation strategy based on customer feedback and changing market conditions.

#### Visualization
- Distribution charts for each cluster.
- Correlation heatmaps to understand feature interdependencies.
- Silhouette analysis charts to evaluate clustering performance.



![image](https://github.com/user-attachments/assets/d4f68c40-a811-40f2-835d-af92f8cc0d97)
![image](https://github.com/user-attachments/assets/2185c5bb-2cd7-466b-ae91-b989ee1d479e)
![image](https://github.com/user-attachments/assets/7ef09ceb-ec17-445d-bf98-7fa06c6aa451)
![image](https://github.com/user-attachments/assets/e8c986f5-af94-4de3-b77f-6ab134f6d57c)
![image](https://github.com/user-attachments/assets/3d4154e0-4cc3-4d50-be11-1500a318fffc)

These documentation sections for Tasks 1,2 and 3 provide a framework for executing and assessing customer satisfaction analysis and segmentation strategies, respectively, using data-driven approaches at Robi Axiata.
