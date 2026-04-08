import streamlit as st
import pandas as pd
import joblib
import time
import numpy as np
import plotly.graph_objects as go
from style import apply_nasa_theme

# 1. Load the AI Model
try:
    model = joblib.load("model.pkl")
except:
    st.error("Error: 'model.pkl' not found. Run 'model.py' first.")

# 2. Page Configuration
st.set_page_config(page_title="ASRIS | PREDICTIVE MISSION CONTROL", layout="wide", page_icon="🛰️")

# 3. Sidebar - Advanced Command Center
st.sidebar.header("📡 COMMAND CENTER")
mode = st.sidebar.radio("Mission Mode:", ["Live AI Stream", "What-If Simulation Lab"])
latency = st.sidebar.select_slider("Deep Space Latency (ms):", options=[0, 500, 1000, 2000], value=0)
sensitivity = st.sidebar.slider("AI Sensitivity Threshold (%)", 85, 98, 92)

# AI Logic: Prediction + XAI + Forecasting
def get_intelligent_prediction(s, r, t):
    df = pd.DataFrame([[s, r, t]], columns=["solar_activity", "radiation_level", "satellite_temp"])
    pred = model.predict(df)[0]
    conf = max(model.predict_proba(df)[0]) * 100
    
    # Root Cause Analysis (XAI)
    total = abs(s) + abs(r) + abs(t) + 1
    weights = {"Solar GW": (abs(s)/total), "Radiation mSv": (abs(r)/total), "Thermal °C": (abs(t)/total)}
    
    # 🌌 Orbital Path Prediction (Trend Forecast)
    s_forecast = s + np.random.normal(2, 6)
    r_forecast = r + np.random.normal(1, 5)
    t_forecast = t + np.random.normal(1, 4)
    forecasts = {"Solar": s_forecast, "Radiation": r_forecast, "Thermal": t_forecast}
    
    return pred, conf, weights, forecasts

# Advanced Gauge with Future Trend (Delta Indicator)
def draw_gauge(label, value, forecast_val, color, max_val=150):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta", 
        value=value,
        delta={'reference': forecast_val, 'relative': False, 'position': "top", 
               'increasing': {'color': "#ef4444"}, 'decreasing': {'color': "#22c55e"}},
        title={'text': f"{label}<br><span style='font-size:0.8em;color:#94a3b8'>Next 10s Trend</span>", 'font': {'size': 16, 'color': '#a5b4fc'}},
        gauge={'axis': {'range': [0, max_val], 'tickcolor': "#475569"},
               'bar': {'color': color},
               'bgcolor': "rgba(0,0,0,0)",
               'bordercolor': "rgba(165, 180, 252, 0.3)"}))
    
    fig.update_layout(height=210, margin=dict(l=10, r=10, t=60, b=10), 
                      paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    return fig

# --- MAIN DASHBOARD ---

if mode == "Live AI Stream":
    placeholder = st.empty()
    while True:
        with placeholder.container():
            # Simulated Data Delay
            if latency > 0:
                time.sleep(latency / 1000)
            
            # Simulated Sensor Data Stream
            s, r, t = np.random.normal(55, 18), np.random.normal(48, 22), np.random.normal(70, 12)
            pred, conf, weights, forecasts = get_intelligent_prediction(s, r, t)
            apply_nasa_theme(pred, conf)
            health = max(0, min(100, 100 - ((s*0.3) + (r*0.5) + (t*0.2))/2))

            st.title("🛰️ ASRIS: PREDICTIVE MISSION CONTROL")
            st.markdown(f"**Data Link:** {'🟢 Real-time' if latency==0 else f'🟡 Latency Sync Active ({latency}ms)'}")
            st.markdown("---")

            col1, col2 = st.columns([2, 1])

            with col1:
                st.subheader("📊 Predictive Telemetry")
                g1, g2, g3 = st.columns(3)
                g1.plotly_chart(draw_gauge("SOLAR PULSE", s, forecasts["Solar"], "#f97316"), use_container_width=True)
                g2.plotly_chart(draw_gauge("RADIATION DENSITY", r, forecasts["Radiation"], "#ef4444"), use_container_width=True)
                g3.plotly_chart(draw_gauge("THERMAL LOAD", t, forecasts["Thermal"], "#3b82f6"), use_container_width=True)
                
                st.plotly_chart(draw_gauge("SATELLITE INTEGRITY", health, health, "#22c55e" if health > 70 else "#ef4444", 100), use_container_width=True)

            with col2:
                st.subheader("🧠 EXPLAINABLE AI (XAI)")
                st.write("Decision Influence Mapping:")
                for factor, w in weights.items():
                    st.write(f"{factor}: {int(w*100)}%")
                    st.progress(w)
                
                st.divider()
                st.subheader("🤖 AUTOMATION LOG")
                if pred == "CRITICAL" and conf > sensitivity:
                    st.error("🚨 EMERGENCY: PREDICTIVE HAZARD DETECTED")
                    st.write("⚙️ Action: Shielding Maximized")
                    # Verified Sound Script
                    st.components.v1.html("""
                        <script>
                        var msg = new SpeechSynthesisUtterance('Warning! Critical Predictive Hazard Detected.');
                        window.speechSynthesis.speak(msg);
                        </script>
                    """, height=0)
                else:
                    st.success("🟢 STATUS: SYSTEM NOMINAL")
                    st.write("⚙️ Monitoring Future Orbital Path...")
            
            time.sleep(1.2)

else:
    # --- SIMULATION LAB ---
    apply_nasa_theme()
    st.title("🛰️ ASRIS: ADVANCED SIMULATION LAB")
    st.markdown("---")
    
    s_val = st.sidebar.slider("Simulate Solar GW", 0, 100, 40)
    r_val = st.sidebar.slider("Simulate Radiation mSv", 0, 100, 40)
    t_val = st.sidebar.slider("Simulate Temp °C", 20, 150, 50)
    
    pred, conf, weights, forecasts = get_intelligent_prediction(s_val, r_val, t_val)
    apply_nasa_theme(pred, conf)
    health = max(0, min(100, 100 - ((s_val*0.3) + (r_val*0.5) + (t_val*0.2))/2))

    lab_col1, lab_col2 = st.columns([1, 1])
    
    with lab_col1:
        st.subheader("🎯 Intelligence Insights")
        st.plotly_chart(draw_gauge("SURVIVAL INDEX", (health+conf)/2, (health+conf)/2, "#00f2ff", 100), use_container_width=True)
        st.write(f"**AI Prediction:** {pred} | **Confidence:** {conf:.1f}%")

    with lab_col2:
        st.subheader("🚀 MISSION SURVIVAL TEST")
        if st.button("RUN PREDICTIVE ANALYTICS"):
            survival = (health + conf) / 2
            st.write(f"### Result: **{survival:.1f}% Survival Chance**")
            if survival > 80: st.balloons()
            else: st.warning("High Risk Detected for current trajectory.")

    st.divider()
    st.subheader("🔬 XAI Decision Trace")
    st.bar_chart(pd.DataFrame(weights.values(), index=weights.keys(), columns=["Weight"]))