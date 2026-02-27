```markdown
# VigilEye 
### Advanced Real-Time Driver Drowsiness Detection System


[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0%2B-green.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-red.svg)](https://google.github.io/mediapipe/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


**A computer vision powered safety solution that monitors driver alertness using facial landmark analysis and audio feedback to prevent fatigue-related accidents.**

---



##  About

VigilEye is an intelligent surveillance system designed to enhance road safety by detecting early signs of driver fatigue. By leveraging the efficiency of **MediaPipe Face Mesh** and the geometric precision of the **Eye Aspect Ratio (EAR)** algorithm, VigilEye provides real-time feedback without the need for heavy hardware or deep learning models.




### The Problem
Driver fatigue is a leading cause of road accidents globally. Microsleeps (unintentional moments of zoning out) can last for seconds but have fatal consequences at high speeds.

### The Solution
VigilEye continuously monitors the driver's eyes via a standard webcam. If the system detects that the eyes have been closed beyond a safe threshold (configurable), it triggers an immediate audible alarm to jolt the driver back to alertness.

---




##  Key Features

- **🚀 High Performance:** Optimized with MediaPipe for sub-millisecond latency on CPU.
- **👁️ Geometric Precision:** Calculates Eye Aspect Ratio (EAR) using 6-point facial landmarks for accurate blink detection.
- **🔊 Audio Feedback:** Integrated Pygame-based alarm system that loops until the driver re-engages.
- **📊 Real-Time Metrics:** Displays live FPS, confidence scores, and an event alert counter.
- **📝 Event Logging:** Automatically timestamps and logs drowsiness events to a local file for review.
- **⚙️ Highly Configurable:** Easily adjust sensitivity and alarm duration via the config file.
- **🧹 Modular Architecture:** Clean, object-oriented codebase separated into utilities, constants, and main logic.

---



## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Computer Vision** | OpenCV |
| **Face Mesh** | Google MediaPipe |
| **Math** | NumPy |
| **Audio** | Pygame |

---



## Project Structure

```text
VigilEye/
│
├── main.py                 # Entry point & Main Application Loop
├── utils/
│   ├── __init__.py
│   ├── ear_calculation.py  # EAR math logic & Landmark indices
│   ├── alarm.py            # Audio handler class
│   └── constants.py        # Configuration thresholds (EAR, Time)
│
├── assets/
│   └── alarm.wav           # Audio trigger file
│
├── logs/                   # Auto-generated: Stores event logs
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- A working webcam
- Virtual Environment (recommended)

- 
### 1. Clone the Repository
```bash
git clone https://github.com/rohitpawar-tech/VigilEye
cd VigilEye
```


### 2. Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```


**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```




### 3. Install Dependencies
```bash
pip install -r requirements.txt
```


### 4. Setup Audio Asset
Place a short sound file named `alarm.wav` inside the `assets/` folder.
*(You can download any royalty-free alarm sound effect online).*

---




##  Usage

Run the application from the root directory:

```bash
python main.py
```


### Controls
- **Close Eyes:** Simulate drowsiness. If closed for >10 seconds (default), alarm triggers.
- **Open Eyes:** Resets the alarm and timer.
- **Press `q`:** Exits the application.

---



## Configuration

You can customize the detection sensitivity by editing `utils/constants.py`:

```python
# Sensitivity: Lower value = more sensitive
EAR_THRESH = 0.21 

# Duration: Seconds eyes must be closed before alarm
DROWSY_DURATION_SEC = 10 
```

---



## The Algorithm

VigilEye computes the **Eye Aspect Ratio (EAR)** to determine eye openness.

$$ EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2||p_1 - p_4||} $$

1. **Detection:** MediaPipe detects 468 facial landmarks.
2. **Extraction:** We isolate 6 specific landmarks for each eye.
3. **Calculation:** We compute the vertical vs. horizontal distances.
4. **Thresholding:**
   - If `EAR < 0.21`, the eye is considered **Closed**.
   - If `EAR > 0.21`, the eye is considered **Open**.
5. **State Machine:** A timer tracks consecutive "Closed" frames. If `time > threshold`, the alarm triggers.

---


## Demo Interface

| State | Visual Indicator |
| :--- | :--- |
| **Awake** | Green eye contours, Status: "AWAKE" |
| **Drowsy Warning** | Red eye contours, Countdown timer displayed |
| **Alarm Active** | Flashing Red UI, Audio playing, Status: "WAKE UP!!" |

---


##  Future Enhancements

- [ ] Yawning detection (mouth aspect ratio)
- [ ] Head pose estimation (detecting if driver is looking at the road)
- [ ] SMS/Email alert integration for fleet management
- [ ] Mobile app deployment (using Kivy or React Native)

---

