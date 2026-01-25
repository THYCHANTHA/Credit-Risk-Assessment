import streamlit as st

def apply_custom_styles():
    """Injects custom CSS for the application."""
    st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@400;700&display=swap');

    /* General Styling */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(15, 20, 30) 0%, rgb(5, 5, 10) 90%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        color: #f0f2f5;
    }

    /* Custom Highlight Class */
    .keyword-highlight {
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        color: white;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
        box-shadow: 0 2px 5px rgba(229, 46, 113, 0.4);
    }

    /* Glassmorphism Containers */
    .glass-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Metrics Container */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 10px;
        padding: 15px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center;
    }

    /* Custom Buttons - Modern Gradient */
    .stButton>button {
        background: linear-gradient(45deg, #4f46e5, #9333ea);
        color: white;
        border: none;
        padding: 12px 28px;
        border-radius: 10px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(147, 51, 234, 0.3);
        filter: brightness(1.1);
    }
    
    /* Secondary Button Style */
    div[data-testid="stColumn"] .stButton>button[kind="secondary"] {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.2);
    }

    /* Progress Bars */
    .stProgress > div > div > div > div {
        background-color: #4f46e5;
        background-image: linear-gradient(315deg, #4f46e5 0%, #9333ea 74%);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 10, 15, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Dataframes */
    .stDataFrame {
         border: 1px solid rgba(255, 255, 255, 0.1);
         border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

def render_header():
    """Renders the main header."""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; animation: fadeIn 1s;">
        <h1 style="background: linear-gradient(to right, #fff, #a5b4fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Dynamic Credit Risk Assessment
        </h1>
        <p style="color: #94a3b8; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
            Next-Generation AI-Powered Risk Analysis for Financial Institutions
        </p>
    </div>
    """, unsafe_allow_html=True)
