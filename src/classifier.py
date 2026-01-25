import streamlit as st
from transformers import pipeline
import torch

@st.cache_resource
def load_zero_shot_model():
    """
    Loads the multilingual zero-shot classification pipeline.
    Cached by Streamlit to prevent reloading on every interaction.
    """
    device = -1  # CPU
    if torch.cuda.is_available():
        device = 0
        
    try:
        # Using 'joeddav/xlm-roberta-large-xnli' for robust multilingual support
        classifier = pipeline(
            "zero-shot-classification", 
            model="joeddav/xlm-roberta-large-xnli", 
            device=device
        )
        return classifier
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None

def predict_risk(text: str, labels: list[str], classifier) -> dict:
    """
    Predicts the risk category for the given text.
    
    Args:
        text (str): The input text (enhanced with English context if needed).
        labels (list): List of candidate labels.
        classifier: The loaded pipeline object.
        
    Returns:
        dict: The result dictionary from the pipeline.
    """
    if not classifier:
        return None
        
    return classifier(text, labels)
