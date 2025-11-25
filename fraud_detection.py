import streamlit as st 
import pandas as pd 
import joblib  

model =joblib.load("fraud_detection_pipeline.pkl") 

st.title("Fraud Detection Prediction App") 

st.markdown("Please Enter the transaction details and use the predict button") 

st.divider() 

