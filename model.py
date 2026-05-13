# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("model/heart.csv")
# EDA

print(data.head())

print(data.info())

print(data.describe())
# Check null values

print(data.isnull().sum())
# Remove null values

data = data.dropna()
# Split features and target

X = data.drop("target", axis=1)
y = data["target"]
# Train Test Split-

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Random Forest Classifier

model = RandomForestClassifier()

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy :", accuracy)

# Save Model

pickle.dump(model, open("heart_model.pkl", "wb"))

print("Model Saved Successfully")