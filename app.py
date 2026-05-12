import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="PetroGuard AI: Sand Control",
    page_icon="🏗️",
    layout="wide"
)

# 2. Load Assets
@st.cache_resource
def load_assets():
    model = joblib.load('sand_model.pkl')
    df = pd.read_csv('sand_data.csv')
    metrics = joblib.load('sand_metrics.pkl')
    return model, df, metrics

try:
    model, df, metrics = load_assets()
except Exception as e:
    st.error("Assets missing! Tabbatar dukkan files suna cikin folder daya.")
    st.stop()

# --- SIDEBAR ---
st.sidebar.image("./images/fudma.webp", width=100)
st.sidebar.title("System Control Center")
st.sidebar.markdown("---")
st.sidebar.write(f"**Field Engineer:** NURA ABDULLAHI")
st.sidebar.write(f"**Matric No:** CSA/2023/27937")
st.sidebar.write(f"**Supervisor:** NURADDEN AHMAD SAMA'ILLA")
st.sidebar.markdown("---")
st.sidebar.success("Software Status: Operational")

# --- MAIN INTERFACE ---
st.title("🏗️ Development of ML Algorithm Tools For Predicting Sand Production")
st.markdown("### *A Geomechanical Decision Support System for Reservoir Integrity*")

# Performance KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Model Reliability (R²)", f"{metrics['r2']*100:.2f}%")
c2.metric("Mean Absolute Error (MAE)", f"{metrics['mae']:.2f} kg/day")
c3.metric("Deployment Zone", "FUDMA Research", delta="Optimized")

st.divider()

# TABS
tab_tool, tab_analytics, tab_docs = st.tabs(["🎯 Prediction Engine", "📊 Statistical Insights", "📑 Methodology & Documentation"])

# --- TAB 1: PREDICTION ENGINE ---
with tab_tool:
    col_input, col_display = st.columns([1, 1.2], gap="large")
    
    with col_input:
        st.subheader("📋 Wellhead Parameters")
        with st.expander("Well Geometry & Flow", expanded=True):
            depth = st.number_input("Vertical Depth (m)", 1000.0, 5000.0, 2500.0)
            flow_rate = st.number_input("Liquid Flow Rate (bpd)", 100.0, 10000.0, 1500.0)
        
        with st.expander("Geomechanical Data", expanded=True):
            pressure = st.number_input("Reservoir Pressure (psi)", 500.0, 10000.0, 3200.0)
            ucs = st.slider("Rock Strength (UCS MPa)", 5.0, 120.0, 45.0)
        
        predict_btn = st.button("🚀 Execute Analysis", use_container_width=True)

    with col_display:
        st.subheader("🔍 Prediction Output")
        if predict_btn:
            with st.spinner('Calculating stress distribution...'):
                time.sleep(1.5)
                features = np.array([[depth, flow_rate, pressure, ucs]])
                prediction = model.predict(features)[0]
                
                # RISK GAUGE CHART
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = prediction,
                    title = {'text': "Predicted Sand (kg/day)"},
                    gauge = {
                        'axis': {'range': [None, 35]},
                        'bar': {'color': "#1f1f1f"},
                        'steps': [
                            {'range': [0, 8], 'color': "#00cc44"},
                            {'range': [8, 18], 'color': "#ffcc00"},
                            {'range': [18, 35], 'color': "#ff3300"}
                        ],
                        'threshold': {'line': {'color': "white", 'width': 4}, 'value': 25}
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)

                # DYNAMIC LOGIC & ACTIONS
                if prediction >= 18:
                    st.error("### 🟥 CRITICAL EROSION RISK")
                    st.markdown("""
                    **Engineering Actions Required:**
                    * Install sand control screens (Gravel Pack).
                    * Reduce flow rate by adjusting choke size.
                    * Monitor borehole stability for potential collapse.
                    """)
                elif prediction >= 8:
                    st.warning("### 🟨 MODERATE PRODUCTION RISK")
                    st.markdown("""
                    **Maintenance Advice:**
                    * Continuous flow-velocity monitoring.
                    * Scheduled sand-cleanout intervals.
                    """)
                else:
                    st.success("### 🟩 OPTIMAL OPERATING WINDOW")
                    st.write("**Operational Status:** Production is safe. No immediate sand control hardware required.")

                # Downloadable Report
                report_text = f"SAND PRODUCTION ANALYSIS REPORT\nField: FUDMA Reservoir\nResult: {prediction:.2f} kg/day\nStatus: {'High' if prediction > 15 else 'Normal'}"
                st.download_button("📥 Download Analysis Report", report_text, file_name="Sand_Analysis.txt")
        else:
            st.info("Input reservoir parameters and click 'Execute Analysis' to begin.")

# --- TAB 2: ANALYTICS ---
with tab_analytics:
    st.subheader("📊 Model Interpretation & Data Correlation")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.write("### 1. Feature Importance (Weights)")
        # Wannan bangaren yana nuna wanne variable ne ya fi tasiri
        try:
            importances = model.feature_importances_
            feat_names = ['Depth', 'Flow Rate', 'Pressure', 'Rock Strength']
            imp_df = pd.DataFrame({'Feature': feat_names, 'Impact': importances}).sort_values(by='Impact')
            fig_imp, ax_imp = plt.subplots()
            sns.barplot(x='Impact', y='Feature', data=imp_df, palette='viridis', ax=ax_imp)
            st.pyplot(fig_imp)
            st.caption("Wannan yana nuna madaidaicin bayanin da model din yake amfani da shi.")
        except:
            st.info("Training data needed for importance plot.")
    
    with col_b:
        st.write("### 2. Feature Correlation Matrix")
        fig1, ax1 = plt.subplots()
        sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='RdYlGn', ax=ax1)
        st.pyplot(fig1)

# --- TAB 3: DOCUMENTATION ---
with tab_docs:
    st.subheader("📖 Project Methodology")
    st.markdown("""
    #### System Architecture:
    1. **Data Source:** Synthetic reservoir data modeled on standard Petroleum Engineering principles.
    2. **Algorithm:** Random Forest Regressor - An ensemble learning method used for its high accuracy in non-linear geological data.
    3. **Key Inputs:** * *Vertical Depth:* Influences overburden pressure.
        * *Flow Rate:* Controls the drag forces on sand grains.
        * *Borehole Pressure:* Affects effective stress.
        * *UCS:* Rock's resistance to mechanical failure.
    """)

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 Federal University Dutsin-Ma | Department of Computer Science | Final Year Project Submission")