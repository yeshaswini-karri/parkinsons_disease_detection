#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from detector import predict_parkinsons
# Streamlit app
st.title('Parkinson\'s Disease Detection')

st.write('Please enter the following details:')
# Add input widgets for features
feature_names = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 
                 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 
                 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 
                 'D2', 'PPE']

input_features = []
for feature_name in feature_names:
    value = st.number_input(f'{feature_name}', step=0.1)
    input_features.append(value)
# Make prediction when 'Predict' button is clicked
if st.button('Predict'):
    prediction = predict_parkinsons(input_features)
    st.write('Prediction:')
    if prediction == 0:
        st.header('PARKINSON\'s NEGATIVE')
    else:
        st.header('PARKINSON\'s POSITIVE')


# In[ ]:




