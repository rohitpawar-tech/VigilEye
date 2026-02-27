import cv2
import mediapipe as mp
import time
import os
import logging
import numpy as np
from datetime import datetime

# Import custom modules
from utils.constants import (
    EAR_THRESH, DROWSY_DURATION_SEC, 
    COLOR_NORMAL, COLOR_ALERT, COLOR_TEXT,
    LOG_FILE_PATH
)
from utils.ear_calculation import calculate_ear, LEFT_EYE_INDICES, RIGHT_EYE_INDICES
from utils.alarm import SoundAlarm

# --- Logging Setup ---
# Ensure logs directory exists
log_dir = os.path.dirname(LOG_FILE_PATH)
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DrowsinessDetector:
    def __init__(self):
        # Initialize Camera
        self.cap = cv2.VideoCapture(0)
        
        # Initialize MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Initialize Alarm
        self.alarm = SoundAlarm(os.path.join(os.path.dirname(__file__), "assets", "alarm.wav"))
        
        # State Variables
        self.start_time = None
        self.alert_counter = 0
        self.is_alarm_active = False

    def process_frame(self, frame):
        """Main logic: Detect face, calculate EAR, determine state."""
        # 1. Preprocessing
        frame = cv2.flip(frame, 1) # Mirror effect
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_h, img_w = frame.shape[:2]
        
        # 2. Face Mesh Detection
        results = self.face_mesh.process(rgb_frame)
        
        status_text = "AWAKE"
        color = COLOR_NORMAL
        
        if results.multi_face_landmarks:
            mesh_points = np.array([
                np.multiply([p.x, p.y], [img_w, img_h]).astype(int) 
                for p in results.multi_face_landmarks[0].landmark
            ])
            
            # Extract Eye Coordinates
            left_eye = mesh_points[LEFT_EYE_INDICES]
            right_eye = mesh_points[RIGHT_EYE_INDICES]
            
            # Calculate EAR
            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0
            
            # Draw Eye Contours (Visual Feedback)
            cv2.polylines(frame, [left_eye], True, COLOR_NORMAL, 1)
            cv2.polylines(frame, [right_eye], True, COLOR_NORMAL, 1)
            
            # 3. Drowsiness Logic
            if avg_ear < EAR_THRESH:
                # Eyes are closed
                if self.start_time is None:
                    self.start_time = time.time()
                
                elapsed_time = time.time() - self.start_time
                remaining_time = max(0, DROWSY_DURATION_SEC - elapsed_time)
                
                status_text = f"DROWSY! ALARM IN: {remaining_time:.1f}s"
                color = COLOR_ALERT
                
                # Update eye color to red
                cv2.polylines(frame, [left_eye], True, COLOR_ALERT, 2)
                cv2.polylines(frame, [right_eye], True, COLOR_ALERT, 2)

                # Check Threshold
                if elapsed_time >= DROWSY_DURATION_SEC:
                    if not self.is_alarm_active:
                        self.trigger_alarm()
                    status_text = "WAKE UP!!!"
            else:
                # Eyes are open
                self.reset_alarm()
        else:
            # No face detected
            self.reset_alarm()

        return frame, status_text, color

    def trigger_alarm(self):
        """Activates alarm and logs the event."""
        self.alarm.start()
        self.is_alarm_active = True
        self.alert_counter += 1
        msg = f"Drowsiness Alert #{self.alert_counter} Triggered!"
        print(f"!!! {msg} !!!")
        logging.warning(msg)

    def reset_alarm(self):
        """Resets timer and stops alarm."""
        self.start_time = None
        if self.is_alarm_active:
            self.alarm.stop()
            self.is_alarm_active = False
            logging.info("Driver woke up. Alarm reset.")

    def draw_ui(self, frame, status_text, color, fps):
        """Overlays text on the video frame."""
        # FPS
        cv2.putText(frame, f"FPS: {int(fps)}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        
        # Alert Counter
        cv2.putText(frame, f"Alerts: {self.alert_counter}", (20, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_TEXT, 2)
        
        # Main Status
        cv2.putText(frame, status_text, (100, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
        
        # EAR Hint
        cv2.putText(frame, f"EAR Thresh: {EAR_THRESH}", (20, 110), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    def run(self):
        """Main Application Loop."""
        logging.info("System Started.")
        prev_time = 0
        
        try:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to grab frame.")
                    break

                # Process Frame
                frame, status_text, color = self.process_frame(frame)
                
                # Calculate FPS
                curr_time = time.time()
                fps = 1 / (curr_time - prev_time)
                prev_time = curr_time
                
                # Render UI
                self.draw_ui(frame, status_text, color, fps)
                
                # Display
                cv2.imshow("Sleep Alarm Driver System", frame)
                
                # Exit on 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except KeyboardInterrupt:
            print("User interrupted.")
        except Exception as e:
            logging.error(f"Runtime Error: {e}")
            print(f"An error occurred: {e}")
        finally:
            # Cleanup
            self.cap.release()
            cv2.destroyAllWindows()
            self.alarm.stop()
            logging.info("System Stopped.")

if __name__ == "__main__":
    detector = DrowsinessDetector()
    detector.run()