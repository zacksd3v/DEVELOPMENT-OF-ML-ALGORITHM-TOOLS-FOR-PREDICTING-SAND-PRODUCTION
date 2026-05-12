# 🏗️ PetroGuard AI: Sand Production Prediction System

### 🎓 Final Year Project - Federal University Dutsin-Ma (FUDMA)
**Topic:** Development of Machine Learning Algorithm Tools for Predicting Sand Production  
**Researcher:** NURA ABDULLAHI  
**Matric No:** CSA/2023/27937  
**Supervisor:** NURADDEN AHMAD SAMA'ILLA  

---

## 🛢️ Executive Summary
Sand production is a major challenge in the petroleum industry, causing equipment erosion, pipe blockage, and borehole instability. This project utilizes an **Advanced Machine Learning (Random Forest)** approach to predict sand influx volume based on subsurface reservoir parameters. 

The goal is to provide a decision-support tool that helps field engineers implement proactive sand control measures like gravel packing or flow-rate optimization.

## 🌟 Professional Features
- **Real-Time Prediction:** Accurate estimation of sand production in kg/day.
- **Risk Assessment Gauge:** An interactive visual meter (Green/Yellow/Red) for quick risk identification.
- **Feature Importance Analysis:** Visualizes which factors (e.g., Rock Strength vs. Pressure) contribute most to sand failure.
- **Engineering Recommendations:** Automated technical advice (e.g., install screens, reduce drawdown) based on predicted risk levels.
- **Data Analytics:** Built-in EDA (Exploratory Data Analysis) to understand reservoir correlations.

## 📊 Core Parameters Analyzed
- **Vertical Depth (m):** To assess overburden stress.
- **Flow Rate (bpd):** To measure fluid drag forces.
- **Well Pressure (psi):** To monitor reservoir energy.
- **Rock Strength (UCS MPa):** To evaluate the mechanical integrity of the formation.

## 🛠️ Technology Stack
- **AI Core:** Random Forest Regressor (Scikit-Learn).
- **Interface:** Streamlit (UI/UX Design).
- **Visualization:** Plotly (Interactive Gauges), Seaborn & Matplotlib (Statistical Charts).
- **Storage:** Joblib (Model Serialization).

## 📂 Project Structure
```text
├── app.py                # Main Streamlit Dashboard
├── sand_model.pkl        # Trained Random Forest Model
├── sand_data.csv         # Reservoir Dataset
├── sand_metrics.pkl      # Evaluation Scores (R² & MAE)
└── images/
    └── fudma.webp        # University Logo