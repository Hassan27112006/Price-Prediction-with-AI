"""
layout.py

Contains functions that control the main layout and visual elements of the app.
"""

import streamlit as st

def show_title():
    """
    Display the main title of the app.
    """
    st.title("🏠 Real Estate Price Prediction App")

def display_prediction(price):
    """
    Show the predicted price.

    Parameters:
    - price (float): Predicted house price.
    """
    st.success(f"💰 Estimated Price: Rs{price:,.2f}")

def display_recognized_text(text):
    """
    Display the recognized voice input.

    Parameters:
    - text (str): Text recognized from speech.
    """
    st.write(f"Recognized: {text}")

def display_voice_response(response):
    """
    Display the assistant's voice response.

    Parameters:
    - response (str): Text response from the assistant.
    """
    st.success(f"Assistant: {response}")
