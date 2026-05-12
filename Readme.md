---

## Sand Production Prediction

Wannan README ɗin an tsara shi ne don ya nuna **Technical Depth** na aikin Petroleum Engineering.

```markdown
# 🏗️ PetroGuard AI: Sand Production Prediction Tool

### 🎓 Final Year Project - Department of Computer Science, FUDMA
**Topic:** Development of Machine Learning Algorithm Tools for Predicting Sand Production  
**Researcher:** Nura Abdullahi  
**Supervisor:** Nuradden Ahmad Sama'illa

---

## 🛢️ Executive Summary
In the oil and gas industry, sand production is a critical challenge that leads to equipment erosion and borehole instability. This project utilizes the **Random Forest Regressor** algorithm to predict sand influx based on geomechanical reservoir parameters, enabling engineers to implement timely sand control measures.

## 🌟 Key Features
- **Advanced Simulation:** Predicts sand volume (kg/day) using reservoir depth, flow rate, and pressure.
- **Risk Assessment Gauge:** A visual "Risk Meter" (Red/Yellow/Green) for immediate decision support.
- **Feature Importance:** Visualizes which reservoir parameters (e.g., Rock Strength) most influence sand influx.
- **Engineering Recommendations:** Provides automated advice on installing sand screens or adjusting choke sizes.

## 📊 Parameters Analyzed
- **TVD:** True Vertical Depth (m)
- **Flow Rate:** Liquid production velocity (bpd)
- **BHP:** Bottom-hole Pressure (psi)
- **UCS:** Unconfined Compressive Strength (Rock Strength in MPa)

## 🏗️ Model Architecture
- **Algorithm:** Random Forest Regressor (Ensemble Learning)
- **Evaluation:** R-Squared (Accuracy) and Mean Absolute Error (MAE).

## 🚀 How to Run
1. Ensure you have the following files in one directory:
   - `app.py`, `sand_model.pkl`, `sand_data.csv`, `sand_metrics.pkl`
2. Run via terminal:
   ```bash
   streamlit run app.py