# app.py

# ❤️ Heart Disease Prediction App using Random Forest + Streamlit

# Import libraries
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("model/heart.csv")

# Remove null values
df = df.dropna()

# Features and Target
x = df.drop("target", axis=1)
y = df["target"]
# Train Model
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=50
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=50
)

model.fit(x_train, y_train)
# Streamlit UI
st.title(" Heart Disease Prediction ❤️ ")

st.write("Enter patient details below:")

# Input fields
age = st.number_input("Age", 1, 120, 25)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate", 50, 250, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame([[
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach, exang,
        oldpeak, slope, ca, thal
    ]], columns=x.columns)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Person has Heart Disease")
    else:
        st.success("✅ Person does NOT have Heart Disease")