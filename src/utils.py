import re

def map_keywords_khmer(text: str) -> tuple[str, str, bool]:
    """
    Detects Khmer text and maps key financial terms to English
    to assist the zero-shot classifier.
    
    Args:
        text (str): Input text.
        
    Returns:
        tuple: (enhanced_text_for_model, highlighted_html_for_ui, is_khmer_bool)
    """
    # Simple regex to check for Khmer Unicode range
    is_khmer = bool(re.search(r'[\u1780-\u17FF]', text))
    
    enhanced_text = text
    keyword_map = {
        "ឥណបត្រ": "loan",
        "បំណុល": "debt",
        "បង់": "pay",
        "បន្ទាន់": "urgent",
        "ប្រាក់": "money/cash",
        "ចំណូល": "income",
        "ចំណាយ": "expense",
        "ធនាគារ": "bank",
        "កម្ចី": "loan"
    }
    
    highlighted_text = text
    
    if is_khmer:
        for original, replacement in keyword_map.items():
            if original in enhanced_text:
                # Add English context for the model, keep original for display
                # We append the English meaning next to the Khmer word
                enhanced_text = enhanced_text.replace(original, f"{original} ({replacement})")
                
                # Prepare highlighted display for UI
                highlighted_text = highlighted_text.replace(
                    original, 
                    f"<span class='keyword-highlight'>{original}</span>"
                )
    
    return enhanced_text, highlighted_text, is_khmer
