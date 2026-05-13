❤️ Heart Disease Prediction using Machine Learning
📌 Overview

The Heart Disease Prediction System is a Machine Learning-based web application developed to predict the likelihood of heart disease using patient medical data. The project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, model building, evaluation, and deployment.

The application is built using Python, Scikit-learn, and Streamlit, providing an interactive interface for users to input health parameters and receive prediction results instantly.

🚀 Features
Data preprocessing and cleaning
Exploratory Data Analysis (EDA)
Machine Learning model training and evaluation
Heart disease risk prediction
Interactive Streamlit web application
User-friendly interface
Real-time prediction output
🛠️ Tech Stack
Technology	Purpose
Python	Programming Language
Pandas	Data Manipulation
NumPy	Numerical Computation
Matplotlib & Seaborn	Data Visualization
Scikit-learn	Machine Learning
Streamlit	Web Application Deployment
Pickle	Model Serialization
📂 Project Structure
Heart_Disease_Prediction/
│
├── app.py
├── model/
│   ├── heart.csv
│   └── model.pkl
│
├── requirements.txt
├── README.md
└── notebooks/
📊 Dataset Information

The dataset contains various medical attributes used to predict heart disease, including:

Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol Level
Fasting Blood Sugar
Resting ECG Results
Maximum Heart Rate Achieved
Exercise-Induced Angina
ST Depression
Number of Major Vessels
Thalassemia
Target Variable
0 → No Heart Disease
1 → Presence of Heart Disease
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/shalinikothapalli29-rgb/Heart_Disease_Prediction.git
2. Navigate to the Project Directory
cd Heart_Disease_Prediction
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
streamlit run app.py
🧠 Machine Learning Workflow
Data Collection
Data Cleaning & Preprocessing
Exploratory Data Analysis
Feature Selection
Model Training
Model Evaluation
Deployment with Streamlit
📈 Model Performance

The project uses the Random Forest Classifier for prediction and achieves strong performance on the testing dataset.

Evaluation Metrics
Accuracy Score
Confusion Matrix
Classification Report
💻 Application Preview

The web application allows users to:

Enter patient health details
Predict heart disease risk instantly
View prediction results through a simple interface
🔮 Future Enhancements
Improve model accuracy using advanced algorithms
Add multiple ML model comparisons
Deploy on cloud platforms like Heroku or Render
Integrate database support
Add authentication and patient history tracking
Create interactive dashboards
