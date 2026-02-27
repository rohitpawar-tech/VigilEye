import os

# --- Path Configuration ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALARM_SOUND_PATH = os.path.join(BASE_DIR, "assets", "alarm.wav")
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "drowsiness_log.txt")

# --- Detection Thresholds ---
# Eye Aspect Ratio below this value indicates eye is closed
EAR_THRESH = 0.21

# Time (in seconds) eyes must be closed to trigger alarm
# (Change to 2.0 for testing purposes, 10.0 for production)
DROWSY_DURATION_SEC = 10 

# --- UI Colors (BGR format for OpenCV) ---
COLOR_NORMAL = (0, 255, 0)   # Green
COLOR_ALERT = (0, 0, 255)    # Red
COLOR_TEXT = (255, 255, 255) # White