# 🚗 VigilEye  
### Intelligent Real-Time Driver Drowsiness Detection System  

<p align="center">
  <b>AI-powered computer vision system for real-time driver fatigue monitoring and accident prevention.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/MediaPipe-FaceMesh-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

## 🧠 Overview

**VigilEye** is a lightweight yet powerful driver monitoring system that detects fatigue using facial landmark geometry.

Instead of relying on heavy deep learning models, VigilEye leverages:

- ⚡ MediaPipe Face Mesh (468 landmark detection)
- 📐 Eye Aspect Ratio (EAR) algorithm
- 🔊 Real-time audio feedback system

Designed for performance, portability, and real-world usability.

---

## 🚨 The Problem

Driver fatigue contributes to thousands of road accidents annually.

Even a 3–5 second microsleep at highway speeds can result in catastrophic consequences.

Traditional solutions require expensive hardware.

---

## 💡 The Solution

VigilEye transforms a simple webcam into an intelligent safety monitor:

1. Detects face in real-time  
2. Extracts eye landmarks  
3. Computes Eye Aspect Ratio  
4. Tracks prolonged eye closure  
5. Triggers alarm if unsafe threshold is crossed  

No GPU. No cloud. No heavy model.  
Pure optimized computer vision.

---

## ✨ Key Features

- 🚀 **Real-Time Performance** – Sub-millisecond inference on CPU
- 👁️ **Precision Eye Tracking** – 6-point EAR geometry
- 🔊 **Emergency Audio Alert** – Persistent alarm until driver responds
- 📊 **Live Metrics Overlay** – FPS, EAR value, alert counter
- 📝 **Automatic Event Logging** – Timestamped fatigue events
- ⚙️ **Configurable Sensitivity** – Adjust thresholds easily
- 🧩 **Modular Codebase** – Clean, scalable architecture

---

## 🏗 Architecture

```
Webcam Feed
     ↓
MediaPipe Face Mesh
     ↓
Eye Landmark Extraction
     ↓
EAR Calculation
     ↓
Threshold Monitoring
     ↓
Alarm + UI Feedback + Logging
```

---

## 🛠 Technology Stack

| Layer | Technology |
|------|------------|
| Language | Python 3.8+ |
| Computer Vision | OpenCV |
| Landmark Detection | MediaPipe Face Mesh |
| Numerical Processing | NumPy |
| Audio System | Pygame |

---

## 📂 Project Structure

```
VigilEye/
│
├── main.py
├── utils/
│   ├── ear_calculation.py
│   ├── alarm.py
│   └── constants.py
│
├── assets/
│   └── alarm.wav
│
├── logs/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/rohitpawar-tech/VigilEye
cd VigilEye
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python main.py
```

Press **Q** to exit.

---

## ⚙️ Configuration

Modify detection sensitivity inside:

```
utils/constants.py
```

```python
EAR_THRESH = 0.21
DROWSY_DURATION_SEC = 10
```

Lower threshold → More sensitive  
Higher threshold → Less sensitive  

---

## 🧮 The Core Algorithm

Eye Aspect Ratio:

\[
EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2||p_1 - p_4||}
\]

If EAR < threshold for defined duration → Alarm triggered.

This geometric method provides fast and reliable blink/drowsiness detection.

---

## 📊 System States

| Status | Indicator |
|--------|----------|
| Awake | Green eye contour |
| Warning | Red contour + countdown |
| Alarm Active | Flashing red UI + audio alert |

---

## 🚀 Future Roadmap

- Yawn detection (Mouth Aspect Ratio)
- Head pose estimation
- Driver attention scoring
- Fleet monitoring dashboard
- Mobile deployment version

---

## 🎯 Resume-Ready Description

Developed a real-time Driver Drowsiness Detection System using MediaPipe Face Mesh and geometric Eye Aspect Ratio analysis. Implemented threshold-based fatigue detection with emergency alarm triggering and event logging optimized for low-latency CPU inference.

---

## 👨‍💻 Author

**Rohit Pawar**  
Computer Vision Engineer | Python Developer  

<p align="center">
  Built to make roads safer 🚦
</p>
