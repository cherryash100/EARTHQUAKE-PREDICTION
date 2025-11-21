# EARTHQUAKE-PREDICTION & LIVE MAP
emoji: 🌎
colorFrom: blue
colorTo: red
sdk: gradio
sdk_version: 5.46.1
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Earthquake Prediction & Live Map

This project provides a machine learning-based earthquake predictor along with a live interactive earthquake map. Users can predict earthquake magnitudes based on latitude and longitude and visualize recent seismic activities in real-time using live API data.

## Features

- **Earthquake Predictor:** Predict earthquake magnitude using latitude and other parameters.
- **Live Earthquake Map:** Interactive map showing recent earthquakes worldwide.
- **Seamless Integration:** Predictor and live map work simultaneously without interruption.
- **Gradio Interface:** Easy-to-use web interface for user interaction.

## Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
python app.py

# 🌍 Earthquake Prediction & Live Global Earthquake Map  

## 📌 Project Overview  
This project combines **machine learning prediction** with a **live interactive map** of earthquakes.  
- The **predictor** uses historical seismic data (latitude, longitude, depth) to estimate earthquake magnitudes.  
- The **live map** fetches real-time earthquake events worldwide using the **USGS Earthquake API**, providing users with up-to-date seismic activity visualization.  
- Built with **Python, Gradio, Folium, Skops, and Hugging Face Spaces**.  

The system demonstrates how data science and visualization can contribute to **seismic risk assessment** and **disaster preparedness**.  

---

## 🚀 Features  
✅ Predict earthquake magnitude from user input (**Latitude, Longitude, Depth**)  
✅ Interactive **dark-themed UI** with animations  
✅ **Live Global Earthquake Map** (updates from USGS API)  
✅ Downloadable **trained model (.skops)** for reproducibility  
✅ Deployed free on **Hugging Face Spaces**  

---

## 📂 Dataset  
- Historical dataset: **SOCR Earthquake Dataset (2017–2019)**  
  - Includes ~18,000 events in California, USA  
  - Features: Date, Time, Latitude, Longitude, Depth, Magnitude  
- Preprocessed to retain essential columns:  
  - `Latitude`, `Longitude`, `Depth`, `Magnitude`  

---

## 🛠️ Tech Stack  
- **Python** (data processing, modeling)  
- **Scikit-learn** (ML models)  
- **Skops** (safe model saving/loading)  
- **Pandas, NumPy** (data handling)  
- **Gradio** (UI/UX interface)  
- **Folium** (interactive maps)  
- **Hugging Face Spaces** (free deployment platform)  

---

## 📊 Model Training  
- Input Features: `Latitude`, `Longitude`, `Depth`  
- Target: `Magnitude`  
- Model: **Linear Regression** (baseline)  
- Performance:  
  - **Mean Squared Error (MSE):** 0.18  
  - **R² Score:** ~0.0074 (low, but expected since earthquakes are highly unpredictable)  
- Saved Model: `earthquake_model.skops`  

---

## 🌐 Live Earthquake Data (API)  
- Integrated with **USGS Earthquake API**:  
  - Endpoint: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`  
  - Provides **real-time global earthquake events** in the last 24 hours.  
- Displayed on an **interactive map** with markers showing:  
  - Magnitude  
  - Location  
  - Time  

---

## 📸 Screenshots  
*(Add some screenshots of your Hugging Face Space UI here)*  

---

## 📦 Installation (Local Setup)  
1. Clone the repository:  
   ```bash
   git clone https://huggingface.co/spaces/your-username/earthquake-prediction
   cd earthquake-prediction
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the app locally:  
   ```bash
   python app.py
   ```  

---

## 🚀 Deployment  
- Hosted on **Hugging Face Spaces** (Gradio + Skops support).  
- Free, unlimited access for users.  

---

## 🔮 Future Enhancements  
- Improve prediction accuracy with **advanced models (Random Forest, XGBoost, Neural Nets)**  
- Train on **global earthquake datasets** instead of California-only  
- Add **7-day or monthly historical earthquake map**  
- Add **real-time alerts** for strong earthquakes (>5.0)  

---

## ⚠️ Disclaimer  
This project is for **educational and research purposes only**.  
Earthquake prediction is an extremely complex task, and this tool does **not guarantee accurate forecasting**. Always rely on official sources (USGS, EMSC, IRIS) for seismic alerts.
