"""
model_utils.py

This module handles loading of the trained ML model, its scaler, and the expected input feature columns.
"""

import pickle

def load_model(path='models/svm_model.pkl'):
    """
    Load the trained model, scaler, and feature columns from a .pkl file.

    Parameters:
    - path (str): Path to the model file.

    Returns:
    - model: The trained SVR model.
    - scaler: The fitted StandardScaler.
    - columns: List of feature columns used during training.
    """
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data['model'], data['scaler'], data['columns']
