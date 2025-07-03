import streamlit as st
import joblib
import numpy as np

model = joblib.load('stock_model.pkl')

st.title("Stock Growth Predictor")

percent_return = st.number_input("1-Year % Return", value=0.0)
volatility = st.number_input("Volatility", value=0.0)

if st.button("Predict"):
    input_data = np.array([[percent_return, volatility]])
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction:")
    st.success(f"The stock is predicted to be **{prediction.upper()}**.")
