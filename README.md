# 🖥️ Sentivault: Real-time NLP Service Engine & Monitor

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![NLP](https://img.shields.io/badge/AI-VADER%20NLP-green.svg)](https://github.com/cjhutto/vaderSentiment)
[![Deployment](https://img.shields.io/badge/Cloud-Render-430098.svg)](https://render.com/)

Sentivault is a production-ready **NLP Inference Service** designed for real-time sentiment analysis and operational system monitoring. Unlike standard AI scripts, Sentivault features a decoupled architecture that separates the processing engine from the administrative monitoring dashboard.

## 🚀 Live Demo
**Access the Service Monitor:** https://sentivault-nlp-monitor.onrender.com
---

## ✨ Key Developer Features
- **Decoupled Architecture:** Modular Python design with a clean separation between the NLP logic (`analyzer.py`) and the UI layer (`app.py`).
- **Live API Simulator:** An integrated "Live Tester" to send raw string payloads to the inference engine and receive structured JSON responses.
- **Operational Audit Trail:** Automated session-based logging using **Pandas** to track every request with timestamps, payloads, and classification metadata.
- **System Health Metrics:** Interactive data visualization via **Plotly** to monitor the distribution of system verdicts and classification accuracy in real-time.
- **Low-Latency Processing:** Optimized using the VADER engine for near-instant (sub-20ms) response times without external API overhead.

---

## 🛠️ Tech Stack
- **Inference Engine:** Python 3.11, VADER Sentiment
- **Dashboard/UI:** Streamlit (React-based Python Framework)
- **Data Layer:** Pandas (Log Management & State Handling)
- **Visualization:** Plotly Express
- **CI/CD & Hosting:** GitHub, Render (Automated Deployment)

---

## 🏗️ System Architecture
1. **Payload Entry:** The user/system sends a text payload through the Dashboard or API simulator.
2. **Logic Execution:** The `analyzer.py` module processes the text using rule-based sentiment reasoning.
3. **Audit Logging:** The system captures the request metadata (Timestamp, Latency, Result) into a Pandas DataFrame.
4. **Visual Monitoring:** The Dashboard pulls the stateful log data to update the Health Charts and Audit Table.

---

## 📸 System Preview

| Live API Tester (JSON) | System Audit Logs | Operational Health Chart |
|-------------------------|-------------------|--------------------------|
<img width="1865" height="925" alt="dashboard_overview" src="https://github.com/user-attachments/assets/01bb4485-d119-4d52-9720-d40b56547c3b" />
<img width="1835" height="884" alt="api_payload_response" src="https://github.com/user-attachments/assets/229da52a-2bd5-44e8-8d4e-a6c73d2742f4" />
<img width="1865" height="921" alt="system_audit_logs" src="https://github.com/user-attachments/assets/fa9f983b-da71-45fc-915d-23b43670c22d" />
<img width="1806" height="840" alt="operational_metrices" src="https://github.com/user-attachments/assets/43536b13-6a12-4405-96dc-3485dedfd7a5" />



## 🛠️ Local Installation
1. **Clone the repository:**
    https://github.com/varshinimopidevi/sentivault-nlp-monitor.git
   Install dependencies:
   pip install -r requirements.txt
   Run the Monitor:
  streamlit run app.py

👤 Author
Varshini Mopidevi
