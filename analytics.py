import csv
import os
from datetime import datetime
from collections import defaultdict
LOG_FILE = "logs/fatigue_events.csv"

class EventLogger:
 def __init__(self):
        self.ensure_log_directory()
        self.ensure_file()
   def ensure_log_directory(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
 def ensure_file(self):
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "timestamp",
                    "event_type",
                    "ear_value",
                    "duration"
                ])
              def log_event(self, event_type, ear_value, duration):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                event_type,
                ear_value,
                duration
            ])
