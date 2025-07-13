"""
voice_handler.py

This module initializes and wraps the voice assistant for use in the app.
"""

from voice import NLPvoiceAssistant

def init_voice_assistant(model_path='models/svm_model.pkl'):
    """
    Create an instance of the voice assistant.

    Parameters:
    - model_path (str): Path to the saved model.

    Returns:
    - NLPvoiceAssistant: Initialized assistant object.
    """
    return NLPvoiceAssistant(model_path)
