"""
input_handler.py

Handles construction and preprocessing of user inputs for prediction.
"""

import pandas as pd

def build_input_df(area, bedrooms, bathrooms, location, columns):
    """
    Construct a DataFrame from user input and align it with the model's expected features.

    Parameters:
    - area (int): Area of the property in square feet.
    - bedrooms (int): Number of bedrooms.
    - bathrooms (int): Number of bathrooms.
    - location (str): Location selected by the user.
    - columns (list): List of columns expected by the model.

    Returns:
    - DataFrame: One-row DataFrame with encoded and ordered features.
    """
    input_data = {
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'location_Countryside': [1 if location == 'Countryside' else 0],
        'location_Downtown': [1 if location == 'Downtown' else 0],
        'location_Suburbs': [1 if location == 'Suburbs' else 0],
    }

    df = pd.DataFrame(input_data)

    # Ensure all expected columns are present
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # Return DataFrame in exact training column order
    return df[columns]
