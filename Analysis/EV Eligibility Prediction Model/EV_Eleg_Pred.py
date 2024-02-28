# Importing necessary libraries for data manipulation and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Importing utilities for splitting the dataset and model evaluation
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Loading the dataset with pandas
db = pd.read_csv(r"C:\Users\hrama\Downloads\Electric_Vehicle_Population_Data.csv")

# Displaying dataset columns and checking for missing values
print(db.columns)
print(db.isnull().sum())

# Dropping rows with missing values to ensure data quality
db = db.dropna()

# Encoding categorical features into dummy/indicator variables and dropping unnecessary columns
df = pd.get_dummies(db, columns=['State', 'City', 'County', 'Make', 'Model', 'Electric Vehicle Type'])
df = df.drop(columns=['VIN (1-10)', 'Vehicle Location', 'Electric Utility'])

# Separating features and the target variable
features = df.drop(columns=['Clean Alternative Fuel Vehicle (CAFV) Eligibility'])
Target = df['Clean Alternative Fuel Vehicle (CAFV) Eligibility']

# Splitting the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, Target, test_size=0.2, random_state=42)

# Initializing and training the Random Forest Classifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Making predictions on the test set
predictions = model.predict(x_test)

# Evaluating the model's accuracy on the test set
print("Accuracy on test set:", accuracy_score(y_test, predictions))

# Correctly using cross_val_score to evaluate the model's performance with cross-validation
# This step evaluates the model's effectiveness across the entire dataset for a more robust metric
scores = cross_val_score(model, features, Target, cv=5)

# Displaying accuracy scores for each fold and the average across all folds
print("Accuracy per fold: ", scores)
print("Average cross-validation accuracy: ", scores.mean())
