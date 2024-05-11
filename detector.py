#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# Load the dataset
df = pd.read_csv('parkinsons.csv')

# Extract features and target variable
X = df.drop(columns=['name','MDVP:Jitter(Abs)','MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'Shimmer:APQ3', 
                 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'status','RPDE', 'DFA', 'spread1', 'spread2', 
                 'D2', 'PPE'], axis=1)
Y = df['status']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = svm.SVC(kernel='linear')
model.fit(X_train, Y_train)

# Function to make prediction
def predict_parkinsons(input_features):
    scaled_features = scaler.transform([input_features])
    prediction = model.predict(scaled_features)
    return prediction[0]

