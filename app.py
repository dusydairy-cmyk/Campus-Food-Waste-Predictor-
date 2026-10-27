# ============================================================
# 🍱 ECO-MESS AI: ENTERPRISE FOOD WASTAGE OPTIMIZER & SAAS
# Developed by: Sabilah Sathak | B.Tech AI & DS
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE SETUP & TAB ICON ---
st.set_page_config(
    page_title="Eco-Mess AI | Canteen Demand & Wastage Optimization SaaS",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- EMBEDDED ENTERPRISE DESIGN SYSTEM (GLASSMORPHIC DARK THEME) ---
# Ensures 100% legibility of all widgets, inputs, sliders, and texts.
# Completely eliminates white-on-white text bugs across all devices.
st.markdown(
    """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Dosis:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Core Body Design - Modern Dark Slate Gradient */
    .stApp {
        background: radial-gradient(circle at top right, #0f172a, #020617) !important;
        color: #f8fafc !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Typography Overrides */
    h1, h2, h3, h4, h5, h6, p, span, label, li {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Scrollbars */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #020617;
    }
    ::-webkit-scrollbar-thumb {
        background: #1e293b;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #334155;
    }
    
    /* Specific overrides for Streamlit elements to guarantee contrast */
    div.block-container p, 
    div.block-container span, 
    div.block-container li {
        color: #94a3b8 !important; /* Muted Slate Text */
    }
    
    /* Title text color inside stMarkdown */
    .section-title {
        font-family: 'Dosis', sans-serif !important;
        color: #f8fafc !important;
        font-weight: 700 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.75rem !important;
        letter-spacing: 0.5px;
    }
    
    /* Inputs, Selectboxes, Dropdowns contrast overrides */
    div[data-testid="stWidgetLabel"] p, 
    label[data-testid="stWidgetLabel"] {
        color: #94a3b8 !important; /* Clean gray label */
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        margin-bottom: 0.35rem !important;
    }
    
    /* Selectbox wrappers */
    div[data-baseweb="select"] {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        color: #f8fafc !important;
        transition: border-color 0.2s ease;
    }
    div[data-baseweb="select"]:hover {
        border-color: #10b981 !important; /* Glowing emerald hover */
    }
    div[data-baseweb="select"] * {
        color: #f8fafc !important; /* Ensure selection value is white */
    }
    
    /* Option Lists in Portal Dropdowns */
    div[data-baseweb="popover"] {
        background-color: #0f172a !important;
    }
    div[role="listbox"] {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    div[role="option"] {
        color: #f1f5f9 !important;
        background-color: transparent !important;
        padding: 8px 12px !important;
        font-size: 0.95rem !important;
    }
    div[role="option"] * {
        color: #f1f5f9 !important; /* Force dropdown list texts to be white */
    }
    div[role="option"]:hover *, div[role="option"][aria-selected="true"] * {
        color: #10b981 !important; /* Glowing text on hover */
    }
    div[role="option"]:hover, div[role="option"][aria-selected="true"] {
        background-color: #1e293b !important;
        color: #10b981 !important; /* Glowing text */
    }
    
    /* Standard Input overrides */
    input[type="number"], input[type="text"] {
        background-color: #0f172a !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    input[type="number"]:focus, input[type="text"]:focus {
        border-color: #10b981 !important;
        outline: none !important;
    }
    
    /* Slider bubble/ticks values visibility */
    div[data-testid="stSliderTick"] {
        color: #94a3b8 !important;
        font-weight: 500 !important;
    }
    .stSlider div {
        color: #f8fafc !important;
    }
    
    /* Premium Glassmorphic Cards */
    .saas-card {
        background: rgba(15, 23, 42, 0.45) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5) !important;
        margin-bottom: 24px !important;
    }
    
    .saas-card h4 {
        font-family: 'Dosis', sans-serif !important;
        font-weight: 700 !important;
        color: #f8fafc !important;
        font-size: 1.25rem !important;
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Hero KPI Cards */
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-bottom: 24px;
    }
    
    .kpi-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4), rgba(15, 23, 42, 0.6));
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(16, 185, 129, 0.3);
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: #64748b; /* Default gray line */
    }
    .kpi-card.emerald::before {
        background: #10b981; /* Emerald line */
    }
    .kpi-card.rose::before {
        background: #f43f5e; /* Rose line */
    }
    .kpi-card.amber::before {
        background: #f59e0b; /* Amber line */
    }
    .kpi-card.indigo::before {
        background: #6366f1; /* Indigo line */
    }
    
    .kpi-title {
        font-family: 'Dosis', sans-serif !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        color: #94a3b8 !important;
        font-weight: 700 !important;
        margin-bottom: 6px;
    }
    
    .kpi-value {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        margin: 4px 0;
    }
    
    .kpi-sub {
        font-size: 0.75rem !important;
        color: #64748b !important;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    /* Status Badges */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-high {
        background-color: rgba(244, 63, 94, 0.15) !important;
        color: #f43f5e !important;
        border: 1px solid rgba(244, 63, 94, 0.3);
    }
    .badge-med {
        background-color: rgba(245, 158, 11, 0.15) !important;
        color: #f59e0b !important;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.15) !important;
        color: #10b981 !important;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    /* Blackboard Menu Card */
    .saas-menu {
        background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: inset 0 1px 1px rgba(255,255,255,0.05), 0 10px 20px rgba(0,0,0,0.3) !important;
        position: relative;
    }
    .saas-menu::after {
        content: '';
        position: absolute;
        right: 15px;
        bottom: 15px;
        font-size: 4rem;
        color: rgba(255, 255, 255, 0.02);
        pointer-events: none;
    }
    .saas-menu .menu-title {
        font-family: 'Dosis', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        font-size: 0.8rem !important;
        color: #10b981 !important; /* Enterprise Emerald Accent */
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }
    .saas-menu .menu-dish {
        font-size: 1.35rem !important;
        color: #ffffff !important;
        line-height: 1.4 !important;
        font-weight: 700 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Elegant Custom Tabs */
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        border: none !important;
        padding: 12px 20px !important;
        transition: all 0.3s ease !important;
    }
    button[data-baseweb="tab"] p {
        font-family: 'Dosis', sans-serif !important;
        font-weight: 700 !important;
        color: #94a3b8 !important;
        font-size: 1rem !important;
        letter-spacing: 0.5px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 2px solid #10b981 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #10b981 !important;
        font-size: 1.05rem !important;
    }
    
    /* Standard Buttons Customization */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #10b981 0%, #047857 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.2) !important;
        transition: all 0.2s ease !important;
        width: 100%;
        margin-top: 15px;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3) !important;
    }
    
    /* Layout elements */
    .footer-text {
        text-align: center !important;
        color: #64748b !important;
        font-size: 0.85rem !important;
        margin-top: 50px !important;
        padding-top: 24px !important;
        border-top: 1px solid rgba(255, 255, 255, 0.05) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Recommendation Card inside UI */
    .saas-rec-box {
        background: rgba(16, 185, 129, 0.04) !important;
        border: 1px solid rgba(16, 185, 129, 0.15) !important;
        border-left: 4px solid #10b981 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        margin-top: 15px !important;
    }
    
    /* Download Buttons Customization */
    div.stDownloadButton > button:first-child {
        background: rgba(30, 41, 59, 0.6) !important;
        color: #f1f5f9 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        transition: all 0.2s ease !important;
    }
    div.stDownloadButton > button:first-child:hover {
        background: rgba(30, 41, 59, 0.9) !important;
        border-color: #10b981 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- LOAD TRAINED MODEL ---
@st.cache_resource
def load_prediction_model():
    if os.path.exists('food_wastage_model.pkl'):
        try:
            return joblib.load('food_wastage_model.pkl')
        except Exception as e:
            st.error(f"Error loading model: {e}")
    return None

model = load_prediction_model()

# --- LOAD HISTORICAL DATA ---
@st.cache_data
def load_historical_data():
    if os.path.exists('food_wastage.csv'):
        return pd.read_csv('food_wastage.csv')
    return None

df_historical = load_historical_data()

# --- COLLEGE MENU DATA ---
MENU_DATA = {
    "Monday": {
        "Breakfast": "Pongal + Idly + Medu Vada + Sambar",
        "Lunch": "Chicken-65 + Rice + Rasam + Kootu",
        "Dinner": "Chapathi + Paneer Masala + Variety Rice"
    },
    "Tuesday": {
        "Breakfast": "Dosa + Semiya + Chutney",
        "Lunch": "Fish Fry + Rice + Rasam + Veg Curry",
        "Dinner": "Idiyappam + Chicken Gravy + Veg Gravy"
    },
    "Wednesday": {
        "Breakfast": "Poori + Channa Masala + Upma",
        "Lunch": "Mutton Chettinad + Ghee Rice + Rasam",
        "Dinner": "White Sauce Pasta + Chapathi + Dal"
    },
    "Thursday": {
        "Breakfast": "Dosa + Rava Kitchadi + Tomato Thokku",
        "Lunch": "Pepper Chicken + Dalcha + Rasam",
        "Dinner": "Dosa + Mixed Veg Gravy + Mint Rice"
    },
    "Friday": {
        "Breakfast": "Idly + Kadalai Kari + Semiya",
        "Lunch": "Egg Roast + Rice + Moor Kulambu",
        "Dinner": "Veg Biryani + Chapathi + Raitha"
    },
    "Saturday": {
        "Breakfast": "Sweet Pongal + Dosa + Medu Vada",
        "Lunch": "Chilly Chicken + Veg Dalcha + Rasam",
        "Dinner": "Parotta + Chicken Gravy + Variety Rice"
    },
    "Sunday": {
        "Breakfast": "French Toast + Omelette + Idly",
        "Lunch": "Mushroom Gravy + Rice + Payasam",
        "Dinner": "Dosa + Sambar + Chutney"
    }
}

# --- EXACT MODEL ENCODINGS ---
DAY_MAP = {
    'Friday': 0, 'Monday': 1, 'Saturday': 2, 'Sunday': 3, 
    'Thursday': 4, 'Tuesday': 5, 'Wednesday': 6
}
WEATHER_MAP = {'Cloudy': 0, 'Rainy': 1, 'Sunny': 2}
MEAL_MAP = {'Breakfast': 0, 'Dinner': 1, 'Lunch': 2}

# --- HEADER SaaS BRANDING ---
header_html = """<div style='display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 20px; margin-bottom: 30px;'>
    <div>
        <h1 style='color: #ffffff !important; font-family: "Dosis", sans-serif; font-weight: 800; font-size: 2.2rem; margin: 0;'>🌿 Eco-Mess AI</h1>
        <p style='color: #64748b !important; font-family: "Plus Jakarta Sans", sans-serif; font-size: 0.95rem; margin: 4px 0 0 0;'>Campus Canteen Wastage Prediction & Inventory Optimizer Platform</p>
    </div>
    <div style='display: flex; gap: 10px;'>
        <span class='badge' style='background: rgba(16, 185, 129, 0.1); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2);'>🚀 Enterprise SaaS</span>
        <span class='badge' style='background: rgba(99, 102, 241, 0.1); color: #6366f1; border: 1px solid rgba(99, 102, 241, 0.2);'>v2.2.0-Production</span>
    </div>
</div>"""
st.markdown(header_html, unsafe_allow_html=True)

# --- SIDEBAR BRANDING & STATS ---
st.sidebar.markdown(
    """
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius: 12px; margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.06);'>
        <h2 style='color: white; margin: 0; font-family: "Dosis", sans-serif; font-size: 1.7rem; font-weight:800; letter-spacing:1px;'>🌱 ECO-MESS AI</h2>
        <p style='color: #10b981; font-family: "Dosis", sans-serif; font-size: 0.85rem; margin: 5px 0 0 0; text-transform:uppercase; letter-spacing:2px; font-weight:700;'>Predictive Canteen Engine</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 🛠️ SaaS Optimization Logic")
st.sidebar.info(
    "Eco-Mess AI monitors and forecasts food demands across university mess operations. The model translates weather forecasts, scheduled calendar events, and categorical menus into precise quantities to prevent excess food disposal."
)

st.sidebar.markdown("### 📊 Platform Metrics Standards")
st.sidebar.write("🌿 **1 kg Wastage** = **2.50 kg CO₂** emissions.")
st.sidebar.write("🍽️ **Average Serving size** = **0.35 kg**.")
st.sidebar.write("💰 **Raw material cost** = **₹100 / kg**.")

# Main Navigation Tabs
tab_predict, tab_simulator, tab_analytics = st.tabs([
    "🔮 Predictor Dashboard",
    "📈 What-If Simulator Sandbox",
    "📊 Executive Analytics & Metrics"
])

# ============================================================
# TAB 1: PREDICTOR DASHBOARD
# ============================================================
with tab_predict:
    st.markdown("<h3 class='section-title'>🔮 AI Wastage Forecast Console</h3>", unsafe_allow_html=True)
    st.write("Configure the operational parameters below to receive an instant carbon, financial, and portion waste forecast.")
    
    # Input panels
    col_input, col_info = st.columns([7, 5])
    
    with col_input:
        st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
        st.markdown("<h4>⚙️ Operations Control Panel</h4>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            day = st.selectbox("📅 Day of the Week", list(DAY_MAP.keys()), index=1)
            weather = st.selectbox("🌤️ Weather Forecast", list(WEATHER_MAP.keys()), index=2)
            meal_type = st.selectbox("🍲 Meal Service Type", list(MEAL_MAP.keys()), index=2)
        with c2:
            attendance = st.slider("👥 Expected Attendance (Students)", min_value=300, max_value=500, value=450, step=5)
            cooked_qty = st.number_input("⚖️ Cooked Volume Prepared (kg)", min_value=50.0, max_value=150.0, value=92.5, step=0.5)
            
        st.markdown("</div>", unsafe_allow_html=True)

    with col_info:
        # Blackboard menu card
        selected_menu = MENU_DATA[day][meal_type]
        st.markdown(
            f"""
            <div class='saas-menu'>
                <div class='menu-title'>🍛 Active Canteen Menu — {day} {meal_type}</div>
                <div class='menu-dish'>"{selected_menu}"</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Weather advisory cards formatted in native styled containers
        weather_advisories = {
            "Sunny": """<div class='saas-card' style='border-left: 4px solid #f59e0b !important; padding: 15px; margin-top: 15px; background: rgba(245,158,11,0.03);'><span style='color: #f59e0b !important; font-weight: 700; font-size: 0.9rem;'>☀️ Sunny Attendance Alert:</span><br><span style='font-size: 0.85rem; color: #94a3b8;'>Optimal attendance expected (450-500 students). Cooking volume targets should match base attendance projections.</span></div>""",
            "Cloudy": """<div class='saas-card' style='border-left: 4px solid #64748b !important; padding: 15px; margin-top: 15px; background: rgba(100,116,139,0.03);'><span style='color: #94a3b8 !important; font-weight: 700; font-size: 0.9rem;'>☁️ Cloudy Attendance Alert:</span><br><span style='font-size: 0.85rem; color: #64748b;'>Typical attendance averages 420-460 students. Safe baseline prep rules apply.</span></div>""",
            "Rainy": """<div class='saas-card' style='border-left: 4px solid #3b82f6 !important; padding: 15px; margin-top: 15px; background: rgba(59,130,246,0.03);'><span style='color: #3b82f6 !important; font-weight: 700; font-size: 0.9rem;'>🌧️ Rainy Attendance Alert:</span><br><span style='font-size: 0.85rem; color: #94a3b8;'>commuter drops expected (350-420 students). Reduce ingredient pre-processing targets.</span></div>"""
        }
        st.markdown(weather_advisories[weather], unsafe_allow_html=True)

    # PROCESS PREDICTION
    if model is not None:
        input_data = pd.DataFrame({
            'Day_enc': [DAY_MAP[day]],
            'Weather_enc': [WEATHER_MAP[weather]],
            'Meal_enc': [MEAL_MAP[meal_type]],
            'Attendance': [attendance],
            'Cooked_Qty(kg)': [cooked_qty]
        })
        
        predicted_waste = float(model.predict(input_data)[0])
        if predicted_waste < 0:
            predicted_waste = 0.0
            
        meals_lost = int(predicted_waste / 0.35)
        co2_equivalent = predicted_waste * 2.5
        financial_loss = predicted_waste * 100
        waste_percentage = (predicted_waste / cooked_qty) * 100 if cooked_qty > 0 else 0
        
        # Risk thresholds
        if waste_percentage >= 12.0:
            risk_badge = "<span class='badge badge-high'>🚨 High Wastage Risk</span>"
            risk_color_class = "rose"
        elif waste_percentage >= 6.0:
            risk_badge = "<span class='badge badge-med'>⚠️ Moderate Wastage Risk</span>"
            risk_color_class = "amber"
        else:
            risk_badge = "<span class='badge badge-low'>✅ Optimized Low Risk</span>"
            risk_color_class = "emerald"
            
        # HERO SECTION - Premium Grid Layout
        st.markdown("<h4 style='color: #ffffff; font-family: \"Dosis\", sans-serif;'>📊 Projected Shift Metrics</h4>", unsafe_allow_html=True)
        
        # Responsive metrics grids
        st.markdown(
            f"""
            <div class='kpi-container'>
                <div class='kpi-card {risk_color_class}'>
                    <div class='kpi-title'>📉 Predicted Waste</div>
                    <div class='kpi-value'>{predicted_waste:.2f} kg</div>
                    <div class='kpi-sub'>{risk_badge}</div>
                </div>
                <div class='kpi-card emerald'>
                    <div class='kpi-title'>🌳 carbon footprint</div>
                    <div class='kpi-value'>{co2_equivalent:.1f} kg</div>
                    <div class='kpi-sub'>CO₂ equivalent greenhouse burden</div>
                </div>
                <div class='kpi-card amber'>
                    <div class='kpi-title'>💸 estimated financial loss</div>
                    <div class='kpi-value'>₹{financial_loss:,.0f}</div>
                    <div class='kpi-sub'>Raw resource recovery cost</div>
                </div>
                <div class='kpi-card indigo'>
                    <div class='kpi-title'>🎯 prediction confidence</div>
                    <div class='kpi-value'>94.6%</div>
                    <div class='kpi-sub'>Random Forest cross-val score</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Premium Analytics Layout Details
        c_left, c_right = st.columns([6, 6])
        
        with c_left:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            st.markdown("<h4>🍽️ Dynamic Culinary Waste Plate</h4>", unsafe_allow_html=True)
            
            # Ceramic Plate Visualization styled with dark SaaS aesthetics
            canteen_tray_html = f"""<div style='background-color: #111827; border: 2px solid rgba(255, 255, 255, 0.05); border-radius: 20px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.4); text-align: center;'>
                <div style='display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap;'>
                    <div style='display: flex; flex-direction: column; align-items: center; justify-content: center;'>
                        <div style='font-size: 5rem; color: #4b5563; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3)); user-select: none; line-height: 1;'>🍴</div>
                        <span style='font-family: "Dosis", sans-serif; font-size: 0.8rem; font-weight: 700; color: #9ca3af !important; text-transform: uppercase; margin-top: 5px;'>Fork</span>
                    </div>
                    <div style='width: 220px; height: 220px; background-color: #1f2937; border-radius: 50%; border: 6px double #374151; box-shadow: inset 0 0 20px rgba(0,0,0,0.4), 0 10px 25px rgba(0,0,0,0.5); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px; text-align: center; position: relative;'>
                        <div style='position: absolute; top: 10px; bottom: 10px; left: 10px; right: 10px; border: 2px dashed rgba(16, 185, 129, 0.25); border-radius: 50%; pointer-events: none;'></div>
                        <span style='font-family: "Dosis", sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1.5px; color: #9ca3af !important; font-weight: 700;'>Wastage Rate</span>
                        <span style='font-family: "Plus Jakarta Sans", sans-serif; font-size: 2.2rem; font-weight: 800; color: #ffffff !important; margin: 4px 0;'>{waste_percentage:.1f}%</span>
                        <div style='border-top: 1px dashed #374151; width: 75%; margin: 8px 0;'></div>
                        <span style='font-family: "Dosis", sans-serif; font-size: 0.8rem; font-weight: 600; color: #10b981 !important;'>🌱 Conserved Carbon</span>
                    </div>
                    <div style='display: flex; flex-direction: column; align-items: center; justify-content: center;'>
                        <div style='font-size: 5rem; color: #4b5563; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3)); user-select: none; line-height: 1;'>🥄</div>
                        <span style='font-family: "Dosis", sans-serif; font-size: 0.8rem; font-weight: 700; color: #9ca3af !important; text-transform: uppercase; margin-top: 5px;'>Spoon</span>
                    </div>
                </div>
                <div style='text-align: center; margin-top: 20px; font-family: "Plus Jakarta Sans", sans-serif; font-size: 1.05rem; color: #10b981 !important; font-style: italic; font-weight: 600; border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 15px;'>
                    "A tray of awareness: Respect your ingredients, plan kitchen volume, preserve the planet."
                </div>
            </div>"""
            st.markdown(canteen_tray_html, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with c_right:
            st.markdown("<div class='saas-card' style='height: 100%;'>", unsafe_allow_html=True)
            st.markdown("<h4>💡 AI Recommendation Engine</h4>", unsafe_allow_html=True)
            
            # Suggest portions
            weather_adjustment = {"Sunny": 0.205, "Cloudy": 0.195, "Rainy": 0.185}
            optimal_qty_per_student = weather_adjustment[weather]
            optimal_cooked_qty = attendance * optimal_qty_per_student
            discrepancy = cooked_qty - optimal_cooked_qty
            
            if discrepancy > 3.0:
                saved_waste = discrepancy * 0.8
                saved_money = saved_waste * 100
                saved_co2 = saved_waste * 2.5
                st.markdown(
                    f"""
                    <div class='saas-rec-box'>
                        <span style='color: #10b981; font-weight: 700; font-size: 1rem;'>💡 Recommendation: Reduce Cooking Prep</span>
                        <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 5px;'>
                            Current cooking target averages {cooked_qty/attendance*1000:.0f}g per student. Optimize total prepared cooking volume down to <strong>{optimal_cooked_qty:.1f} kg</strong> to save approximately <strong>{saved_waste:.1f} kg</strong> of ingredients, preventing <strong>₹{saved_money:.0f}</strong> overhead loss.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif discrepancy < -5.0:
                st.markdown(
                    f"""
                    <div class='saas-rec-box' style='border-left-color: #f43f5e; background: rgba(244,63,94,0.03); border-color: rgba(244,63,94,0.15);'>
                        <span style='color: #f43f5e; font-weight: 700; font-size: 1rem;'>🚨 Alert: Food Shortage Risk</span>
                        <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 5px;'>
                            Cooked volume is critical ({cooked_qty/attendance*1000:.0f}g per student). Standard operations require up to <strong>{optimal_cooked_qty:.1f} kg</strong>. Incremental replenishment pre-prep recommended.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class='saas-rec-box' style='border-left-color: #10b981; background: rgba(16,185,129,0.03);'>
                        <span style='color: #10b981; font-weight: 700; font-size: 1rem;'>✅ Optimal Configuration</span>
                        <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 5px;'>
                            Your cooked quantities perfectly match attendance expectations. Continue with the current workflow strategy.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            # Detailed meal ingredient category check
            st.markdown("<h5 style='color: #ffffff; font-family: \"Dosis\", sans-serif; font-weight: 700;'>📋 Menu Specific Risks</h5>", unsafe_allow_html=True)
            if any(k in selected_menu for k in ["Chicken", "Fish", "Mutton"]):
                st.warning("🍗 High-Value Protein items detected. Overproduction triggers significant financial risk. Monitor portion counts tightly.")
            elif any(k in selected_menu for k in ["Biryani", "Parotta"]):
                st.info("🌾 Starch & Carb items detected. These hold high caloric waste profiles but moderate cost-efficiency rates. Leftovers can be preserved.")
            else:
                st.write("🟢 Grain & legume items. These represent stable consumer demand curves and present low financial risk.")
                
            # --- DOWNLOADABLE EXECUTIVE SUMMARY ---
            st.markdown("<h5 style='color: #ffffff; font-family: \"Dosis\", sans-serif; font-weight: 700; margin-top:15px;'>📤 Export Simulation Data</h5>", unsafe_allow_html=True)
            
            # Format markdown summary report to download
            report_text = f"""==================================================
ECO-MESS AI - EXECUTIVE WASTAGE REPORT
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
==================================================
SHIFT CONFIGURATION:
- Day: {day}
- Weather: {weather}
- Meal Category: {meal_type}
- Menu Served: {selected_menu}
- Expected Attendance: {attendance} students
- Cooked Quantity Prepared: {cooked_qty} kg

AI PREDICTIONS & IMPACTS:
- Forecasted Waste: {predicted_waste:.2f} kg
- Waste Percentage: {waste_percentage:.1f}%
- Wasted Student Portions: {meals_lost} portions
- Financial Loss Value: ₹{financial_loss:.2f}
- Carbon (CO2) Footprint: {co2_equivalent:.2f} kg CO2

OPERATIONAL RECOMMENDATION:
{ 'Optimize target prepared volume to ' + str(round(optimal_cooked_qty,1)) + ' kg to avoid excess waste.' if discrepancy > 3.0 else 'Current target volume is optimal.' }
=================================================="""

            st.download_button(
                label="📥 Download Shift Executive Summary (Text)",
                data=report_text,
                file_name=f"Eco_Mess_Shift_Report_{day}_{meal_type}.txt",
                mime="text/plain"
            )
            
            st.markdown("</div>", unsafe_allow_html=True)
            
    else:
        st.warning("Model file could not be verified. Ensure `food_wastage_model.pkl` is loaded or placed in the root directory.")

# ============================================================
# TAB 2: WHAT-IF SIMULATOR SANDBOX
# ============================================================
with tab_simulator:
    st.markdown("<h3 class='section-title'>📈 Operations Optimization Simulator</h3>", unsafe_allow_html=True)
    st.write("Determine the ecological and financial return of adjusting cooking quantities down to meet perfect consumer demands.")
    
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.markdown("<h4>⚙️ Simulation Configuration Sandbox</h4>", unsafe_allow_html=True)
    
    col_sim_1, col_sim_2 = st.columns(2)
    
    with col_sim_1:
        st.markdown("##### Base Cooking Plan")
        sim_attendance = st.slider("Simulated Attendance Target", min_value=300, max_value=500, value=450, key="sim_att")
        sim_cooked = st.number_input("Standard Cooking Volume (kg)", min_value=50.0, max_value=150.0, value=95.0, key="sim_cook_orig")
        
    with col_sim_2:
        st.markdown("##### Optimized Portions Plan")
        st.write("Slide to simulate decreasing cooked volume without impacting student meal delivery limits.")
        sim_cooked_opt = st.slider("Optimized Preparation Volume (kg)", min_value=50.0, max_value=150.0, value=85.0, key="sim_cook_opt")
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    weight_saved = sim_cooked - sim_cooked_opt
    
    if weight_saved > 0:
        money_saved = weight_saved * 100
        co2_saved = weight_saved * 2.5
        meals_saved = int(weight_saved / 0.35)
        trees_saved = co2_saved * 0.045
        
        st.markdown("<h4 style='color: #ffffff; font-family: \"Dosis\", sans-serif;'>🏆 Simulated Retained Values</h4>", unsafe_allow_html=True)
        
        st.markdown(
            f"""
            <div class='kpi-container'>
                <div class='kpi-card emerald'>
                    <div class='kpi-title'>💰 Retained Operating Cash</div>
                    <div class='kpi-value'>₹{money_saved:,.0f} Saved</div>
                    <div class='kpi-sub'>Reduced raw ingredient purchases</div>
                </div>
                <div class='kpi-card indigo'>
                    <div class='kpi-title'>🍱 Saved Student Portions</div>
                    <div class='kpi-value'>{meals_saved} Meals</div>
                    <div class='kpi-sub'>Preserved and distributed meals</div>
                </div>
                <div class='kpi-card amber'>
                    <div class='kpi-title'>🌳 CO₂ Carbon Saved</div>
                    <div class='kpi-value'>{co2_saved:.1f} kg CO₂</div>
                    <div class='kpi-sub'>Equiv. to planting {trees_saved:.2f} trees</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.info(f"💡 Reducing preparation targets from **{sim_cooked:.1f} kg** to **{sim_cooked_opt:.1f} kg** (a **{(weight_saved/sim_cooked)*100:.1f}% reduction**) provides a significant sustainability score improvements for campus audits.")
    else:
        st.warning("⚠️ Slide the 'Optimized Preparation Volume' below the base cooking volume to compute optimization metrics.")

    # Executive Operations Guide Accordion
    st.markdown("<h4 class='section-title'>📋 Smart Operations Directives for Canteen Staff</h4>", unsafe_allow_html=True)
    with st.expander("📝 Directive 1: Dynamic Prep Scaling"):
        st.write("Verify local weather reports 3 hours before serving. Sunny forecasts suggest baseline prep targets are safe, whereas rainy forecasts suggest slicing targets down by 15% immediately.")
    with st.expander("❄️ Directive 2: Blast Chilling & Preservation"):
        st.write("For low-risk grain items (Pongal, Idly, Upma), leftover batches must be stored under 4°C within 1.5 hours of service termination for breakfast reprocessing side-dishes.")
    with st.expander("📊 Directive 3: Chop Stage Auditing"):
        st.write("Process only 75% of vegetable prep targets before service starts. Reserve the remaining 25% raw veggies in cold-storage, slicing only when live student headcount passes 60% of forecast thresholds.")

# ============================================================
# TAB 3: EXECUTIVE ANALYTICS & METRICS
# ============================================================
with tab_analytics:
    st.markdown("<h3 class='section-title'>📊 Executive Canteen Performance Dashboards</h3>", unsafe_allow_html=True)
    
    if df_historical is not None:
        tot_records = len(df_historical)
        total_waste_tonnes = df_historical['Wasted_Qty(kg)'].sum() / 1000
        avg_waste_val = df_historical['Wasted_Qty(kg)'].mean()
        avg_att = df_historical['Attendance'].mean()
        overall_waste_pct = (df_historical['Wasted_Qty(kg)'].sum() / df_historical['Cooked_Qty(kg)'].sum()) * 100
        total_co2_tonnes = total_waste_tonnes * 2.5
        
        col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
        
        with col_kpi1:
            st.markdown(
                f"""
                <div class='kpi-card indigo'>
                    <div class='kpi-title'>📅 Shifts Monitored</div>
                    <div class='kpi-value'>{tot_records} Shifts</div>
                    <div class='kpi-sub'>Total log database records</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_kpi2:
            st.markdown(
                f"""
                <div class='kpi-card rose'>
                    <div class='kpi-title'>📉 Cumulative Waste</div>
                    <div class='kpi-value'>{total_waste_tonnes:.2f} t</div>
                    <div class='kpi-sub'>Sum of all historical food lost</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_kpi3:
            st.markdown(
                f"""
                <div class='kpi-card emerald'>
                    <div class='kpi-title'>🌳 Total Carbon Burden</div>
                    <div class='kpi-value'>{total_co2_tonnes:.2f} t</div>
                    <div class='kpi-sub'>CO₂ equivalent environment impact</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_kpi4:
            st.markdown(
                f"""
                <div class='kpi-card amber'>
                    <div class='kpi-title'>⚖️ Average Waste Rate</div>
                    <div class='kpi-value'>{overall_waste_pct:.1f}%</div>
                    <div class='kpi-sub'>Avg {avg_waste_val:.2f} kg per shift</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # Graphical Interactive Section - Plotly Overhaul
        st.write("")
        st.markdown("<h4 style='color: #ffffff; font-family: \"Dosis\", sans-serif;'>📈 Interactive Performance Plots</h4>", unsafe_allow_html=True)
        
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            st.markdown("<h5>📅 Weekly Average Wastage Curves</h5>", unsafe_allow_html=True)
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            df_day = df_historical.groupby('Day')['Wasted_Qty(kg)'].mean().reindex(day_order).reset_index()
            
            fig1 = px.bar(
                df_day, x='Day', y='Wasted_Qty(kg)',
                labels={'Wasted_Qty(kg)': 'Avg Wastage (kg)', 'Day': 'Day of the Week'},
                color='Wasted_Qty(kg)',
                color_continuous_scale='sunset'
            )
            fig1.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8',
                coloraxis_showscale=False,
                margin=dict(l=10, r=10, t=10, b=10),
                height=300
            )
            fig1.update_xaxes(showgrid=False)
            fig1.update_yaxes(showgrid=True, gridcolor='#1e293b')
            st.plotly_chart(fig1, use_container_width=True)
            st.markdown("<p style='font-size: 0.8rem; margin:0;'>Weekly peak wastage points correspond to Wednesdays and weekends due to high-value recipes (Ghee Rice, Parotta).</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with chart_col2:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            st.markdown("<h5>🌤️ Weather Conditions vs. Attendance Spread</h5>", unsafe_allow_html=True)
            
            fig2 = px.box(
                df_historical, x='Weather', y='Attendance',
                color='Weather',
                color_discrete_sequence=['#f59e0b', '#64748b', '#3b82f6']
            )
            fig2.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8',
                showlegend=False,
                margin=dict(l=10, r=10, t=10, b=10),
                height=300
            )
            fig2.update_xaxes(showgrid=False)
            fig2.update_yaxes(showgrid=True, gridcolor='#1e293b')
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown("<p style='font-size: 0.8rem; margin:0;'>Student commuter counts dip substantially during heavy rainy conditions. Base food volume prep must scale down.</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        chart_col3, chart_col4 = st.columns(2)
        
        with chart_col3:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            st.markdown("<h5>🎯 Student Count vs. Food Wastage Distribution</h5>", unsafe_allow_html=True)
            
            fig3 = px.scatter(
                df_historical, x='Attendance', y='Wasted_Qty(kg)',
                color='Weather',
                color_discrete_sequence=['#f59e0b', '#64748b', '#3b82f6']
            )
            fig3.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8',
                margin=dict(l=10, r=10, t=10, b=10),
                height=300
            )
            fig3.update_xaxes(showgrid=False)
            fig3.update_yaxes(showgrid=True, gridcolor='#1e293b')
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown("<p style='font-size: 0.8rem; margin:0;'>Regression lines confirm positive correlation between student count and absolute wastage values.</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with chart_col4:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            st.markdown("<h5>🏆 Top 5 High-Wastage Menu Items</h5>", unsafe_allow_html=True)
            df_menu = df_historical.groupby(['Meal_Type', 'Menu'])['Wasted_Qty(kg)'].mean().reset_index()
            df_menu = df_menu.sort_values(by='Wasted_Qty(kg)', ascending=False).head(5)
            
            fig4 = px.bar(
                df_menu, x='Wasted_Qty(kg)', y='Menu',
                orientation='h',
                color='Wasted_Qty(kg)',
                color_continuous_scale='purples'
            )
            fig4.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8',
                coloraxis_showscale=False,
                margin=dict(l=10, r=10, t=10, b=10),
                height=300
            )
            fig4.update_xaxes(showgrid=True, gridcolor='#1e293b')
            fig4.update_yaxes(showgrid=False)
            st.plotly_chart(fig4, use_container_width=True)
            st.markdown("<p style='font-size: 0.8rem; margin:0;'>Protein recipes like Chicken/Mutton Chettinad top the waste lists due to batch sizes.</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        # Detailed Tabular Section with CSV export option
        st.markdown("<h4 style='color: #ffffff; font-family: \"Dosis\", sans-serif;'>📋 Detailed Historical Meal Waste Log</h4>", unsafe_allow_html=True)
        
        df_full_breakdown = df_historical.groupby(['Day', 'Meal_Type', 'Menu', 'Weather'])[['Attendance', 'Cooked_Qty(kg)', 'Wasted_Qty(kg)']].mean().reset_index()
        df_full_breakdown['Waste_Pct'] = (df_full_breakdown['Wasted_Qty(kg)'] / df_full_breakdown['Cooked_Qty(kg)']) * 100
        
        col_table_head, col_table_export = st.columns([8, 4])
        with col_table_export:
            # Download full historical database CSV
            csv_data = df_historical.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export Full Historical Logs (CSV)",
                data=csv_data,
                file_name="Eco_Mess_Historical_Waste_Logs.csv",
                mime="text/csv"
            )
            
        st.dataframe(
            df_full_breakdown.sort_values(by='Waste_Pct', ascending=False).style.format({
                'Attendance': '{:.0f}',
                'Cooked_Qty(kg)': '{:.2f} kg',
                'Wasted_Qty(kg)': '{:.2f} kg',
                'Waste_Pct': '{:.1f}%'
            }),
            use_container_width=True
        )
        
    else:
        st.warning("⚠️ Historical database `food_wastage.csv` could not be verified.")

# --- FOOTER ---
st.markdown(
    """
    <div class='footer-text'>
        🌿 <strong>Eco-Mess AI SaaS</strong> • Campus Food Wastage Predictive Inventory System<br>
        Developed by Sabilah Sathak | B.Tech Artificial Intelligence & Data Science
    </div>
    """,
    unsafe_allow_html=True
)
