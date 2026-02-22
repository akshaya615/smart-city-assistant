Got it 👍
You want **your project (Accident Severity + Hotspot Detection)** formatted exactly like your friend’s README style** — same structure, same highlighting style, icons, neat sections, detailed structure — but with YOUR project content.

Here is your README converted properly 👇

---

# 🚦 AI-Powered Real-Time Accident Severity Prediction & Hotspot Detection System

A comprehensive **Real-Time Road Accident Severity Prediction and Hotspot Detection Framework** using **HDBSCAN, XGBoost, GNN, FastAPI, and React** with intelligent **context-aware voice alerts** and interactive geospatial visualization.

---

## 🎯 System Overview

This system predicts accident severity, detects accident-prone hotspots, analyzes route-level risk, and provides real-time contextual voice alerts for safer transportation planning.

It combines **Machine Learning, Graph Neural Networks, Spatial Clustering, and Full-Stack Web Deployment** into one intelligent safety monitoring system.

---

## 🔍 Key Features

### ✅ Real-Time Severity Prediction

* Hybrid model using **XGBoost + Graph Neural Network (GNN)**
* Classifies accidents into **Low, Medium, High severity**
* Returns probability-based predictions

### 📍 Hotspot Detection (HDBSCAN)

* Density-based spatial clustering
* Automatically detects high-risk accident zones
* Ignores noise points intelligently

### 🛣️ Route Risk Evaluation

* Calculates severity-weighted risk score
* Evaluates selected user routes
* Provides dynamic risk insights

### 🔊 Context-Aware Voice Alerts

* Uses Web Speech API
* Triggers alerts when entering high-risk zones
* Enhances real-time road safety

### 🔐 Secure Authentication

* JWT-based authentication
* Role-based dashboards (Admin/User)
* Secure database integration

---

## 🚀 Quick Start

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd project-major
```

---

### 2️⃣ Backend Setup

```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:
**[http://localhost:8000](http://localhost:8000)**

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
**[http://localhost:5173](http://localhost:5173)**

---

## 📁 Complete Project Structure

```
project-major/
│
├── 📂 api/
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   │
│   ├── 📂 routes/
│   │     ├── predict.py
│   │     ├── alerts.py
│   │     ├── hotspots.py
│   │     └── auth.py
│   │
│   ├── 📂 core/
│   │     ├── database.py
│   │     ├── dependencies.py
│   │     ├── security.py
│   │     └── secretkey.py
│   │
│   ├── 📂 jobs/
│   │     ├── scheduler.py
│   │     └── hotspot_job.py
│   │
│   ├── 📂 ml/
│   │     ├── gnn_model.py
│   │     ├── xgboost_model.py
│   │     ├── hybrid_predictor.py
│   │     ├── gnn_model.pt
│   │     ├── xgb_model.pkl
│   │     └── severity_label_encoder.pkl
│   │
│   ├── 📂 preprocessing/
│   │     ├── clean_dataset.py
│   │     ├── feature_engineering.py
│   │     ├── build_graph.py
│   │     └── load_dataset.py
│   │
│   ├── 📂 analytics/
│   │     ├── hdbscan_hotspots.py
│   │     └── kde_heatmap.py
│   │
│   └── 📂 data/
│         ├── accident.csv
│         ├── cleaned_accident.csv
│         ├── processed_accident.csv
│         └── nodes.csv
│
├── 📂 frontend/
│   │
│   ├── 📂 src/
│   │   ├── 📂 components/
│   │   │   ├── LiveMap.jsx
│   │   │   ├── Hotspots.jsx
│   │   │   ├── Alerts.jsx
│   │   │   ├── SeverityPie.jsx
│   │   │   ├── RouteMap.jsx
│   │   │   └── VoiceAlert.jsx
│   │   │
│   │   ├── 📂 pages/
│   │   │   ├── Landing.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── UserDashboard.jsx
│   │   │   └── AdminDashboard.jsx
│   │   │
│   │   └── api/api.js
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🧠 System Architecture

```
Frontend (React + Leaflet)
        ↓
FastAPI Backend (REST APIs)
        ↓
Machine Learning Layer
   • XGBoost Severity Predictor
   • Graph Neural Network
   • Hybrid Predictor
   • HDBSCAN Hotspot Detection
        ↓
Processed Accident Dataset
```

---

## 📊 Core Functional Modules

### 1️⃣ Severity Prediction Module

* Uses trained XGBoost & GNN models
* Hybrid ensemble prediction
* Returns class + probability

---

### 2️⃣ Hotspot Detection Module

* HDBSCAN clustering
* Identifies dense accident zones
* Periodic hotspot recalculation

---

### 3️⃣ Route Risk Analysis Module

* Evaluates user-selected routes
* Computes severity-weighted risk score
* Displays risk overlay on map

---

### 4️⃣ Voice Alert System

* Web Speech API integration
* Real-time risk notifications
* Context-aware alert generation

---

## 📊 API Endpoints

| Endpoint         | Method | Description                 |
| ---------------- | ------ | --------------------------- |
| `/predict`       | POST   | Predict accident severity   |
| `/hotspots`      | GET    | Retrieve clustered hotspots |
| `/alerts`        | GET    | Fetch risk alerts           |
| `/auth/login`    | POST   | User login                  |
| `/auth/register` | POST   | User registration           |
| `/docs`          | GET    | Swagger API documentation   |

---

## 📚 Technologies Used

### 🔹 Backend

* FastAPI
* Uvicorn
* Pydantic
* Python

### 🔹 Machine Learning

* XGBoost
* PyTorch
* HDBSCAN
* Scikit-learn
* Pandas
* NumPy

### 🔹 Frontend

* React
* Vite
* Leaflet.js
* JavaScript (ES6+)
* CSS3

---

## 📈 Model Performance

* Hybrid model improves prediction robustness
* HDBSCAN effectively identifies high-density clusters
* Supports scalable web deployment

---

## 🔄 System Workflow

1. User selects route on map
2. Backend processes route data
3. ML model predicts severity
4. HDBSCAN identifies hotspot zones
5. Risk score is calculated
6. Voice alert triggered (if high-risk)
7. Results displayed on dashboard

---

## 🎓 Educational Value

This project demonstrates:

* Supervised Learning (XGBoost)
* Graph Neural Networks
* Unsupervised Clustering (HDBSCAN)
* Geospatial Data Analysis
* Full-Stack Web Development
* JWT Authentication
* Real-Time Alert Systems

---

## 📄 License

This project is developed for academic and research purposes.

**All Rights Reserved © 2026**

---
