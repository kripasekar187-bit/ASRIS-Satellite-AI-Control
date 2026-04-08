import streamlit as st

def apply_nasa_theme(prediction="SAFE", confidence=95):
    # Dynamic Neon Glow colors based on status
    if prediction == "CRITICAL" and confidence > 92:
        accent_color = "#ff4b4b" # Neon Red
        glow_color = "rgba(255, 75, 75, 0.3)"
    elif prediction == "WARNING":
        accent_color = "#ffaa00" # Neon Orange
        glow_color = "rgba(255, 170, 0, 0.3)"
    else:
        accent_color = "#00f2ff" # Neon Cyan/Blue
        glow_color = "rgba(0, 242, 255, 0.2)"

    # Galaxy Background Image
    bg_image = "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072&auto=format&fit=crop"

    nasa_css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(2, 6, 23, 0.7), rgba(2, 6, 23, 0.7)), url("{bg_image}");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }}
    
    /* Neon Glass Card for Metrics */
    [data-testid="stMetric"] {{
        background: rgba(15, 23, 42, 0.6) !important;
        border: 2px solid {accent_color} !important;
        box-shadow: 0 0 15px {glow_color} !important;
        border-radius: 15px !important;
        padding: 20px !important;
        backdrop-filter: blur(12px);
    }}

    /* Colorful Metric Values */
    [data-testid="stMetricValue"] {{
        color: {accent_color} !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: 800 !important;
        font-size: 2.5rem !important;
    }}

    /* Headers with Glow */
    h1 {{
        color: {accent_color} !important;
        text-shadow: 0 0 10px {glow_color};
        text-transform: uppercase;
        letter-spacing: 5px;
        text-align: center;
    }}

    /* Sidebar vibrant look */
    section[data-testid="stSidebar"] {{
        background-color: rgba(2, 6, 23, 0.95) !important;
        border-right: 2px solid {accent_color};
    }}

    /* Customizing Progress Bar color */
    .stProgress > div > div > div > div {{
        background-color: {accent_color} !important;
    }}
    </style>
    
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(nasa_css, unsafe_allow_html=True)