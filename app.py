"""
app.py

Main entry point for the Streamlit Real Estate Price Prediction App.
Handles user interaction, feature collection, model inference, and voice assistant.
"""

import streamlit as st
import pickle
from load import load_model
from handler import build_input_df
from voicehandel import init_voice_assistant
from sidebar import sidebar_inputs
from layout import show_title, display_prediction, display_recognized_text, display_voice_response

# 📌 Display main title
show_title()

# 📥 Load model, scaler, and feature columns
model, scaler, columns = load_model()

# 🎛 Collect user inputs
area, bedrooms, bathrooms, location = sidebar_inputs()

# 🧠 Prepare and scale input data
input_df = build_input_df(area, bedrooms, bathrooms, location, columns)
input_scaled = scaler.transform(input_df)

# 🔮 Predict price
if st.button("🔮 Predict Price"):
    prediction = model.predict(input_scaled)
    display_prediction(prediction[0])

# 🎤 Handle voice interaction
assistant = init_voice_assistant()

if st.button("🎤 Ask via Voice"):
    st.write("Listening...")
    user_input = assistant.listen()
    display_recognized_text(user_input)
    response = assistant.get_response(user_input)
    display_voice_response(response)
