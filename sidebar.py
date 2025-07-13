"""
sidebar.py

Creates the Streamlit sidebar UI for collecting property details from the user.
"""

import streamlit as st

def sidebar_inputs():
    """
    Display sidebar widgets to collect property features.

    Returns:
    - area (int): Area input by the user.
    - bedrooms (int): Number of bedrooms.
    - bathrooms (int): Number of bathrooms.
    - location (str): Selected location.
    """
    st.sidebar.header("📋 Input Property Details")

    area = st.sidebar.number_input("Area (in sq ft)", min_value=100, max_value=10000, value=1500)
    bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.sidebar.slider("Bathrooms", 1, 10, 2)
    location = st.sidebar.selectbox("Location", ['Downtown', 'Suburbs', 'Countryside'])

    st.sidebar.markdown("---")
    st.sidebar.header("🎤 Voice Assistant")

    return area, bedrooms, bathrooms, location
