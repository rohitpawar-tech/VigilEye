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

def read_events(self):
        events = []

        if not os.path.exists(LOG_FILE):
            return events

        with open(LOG_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                events.append(row)

        return events

class FatigueAnalytics:

    def __init__(self):
        self.logger = EventLogger()

    def total_events(self):
        events = self.logger.read_events()
        return len(events)

    def events_by_day(self):
        events = self.logger.read_events()

        stats = defaultdict(int)

        for e in events:
            date = e["timestamp"].split(" ")[0]
            stats[date] += 1

        return dict(stats)

    def average_ear(self):
        events = self.logger.read_events()

        if not events:
            return 0
  total = 0

        for e in events:
            total += float(e["ear_value"])

        return total / len(events)
