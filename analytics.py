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

  def longest_drowsy_event(self):
        events = self.logger.read_events()

        longest = 0

        for e in events:
            duration = float(e["duration"])

            if duration > longest:
                longest = duration

        return longest
 def print_summary(self):
        print("\n===== FATIGUE ANALYTICS REPORT =====\n")

        print("Total Events:", self.total_events())

        print("\nEvents Per Day:")
        stats = self.events_by_day()

        for day, count in stats.items():
            print(day, ":", count)

        print("\nAverage EAR:", round(self.average_ear(), 3))

        print("Longest Drowsy Event:", self.longest_drowsy_event(), "seconds")

        print("\n====================================\n")

class SessionTracker:

    def __init__(self):
        self.start_time = datetime.now()
        self.events = []

    def add_event(self, ear, duration):
        self.events.append({
            "ear": ear,
            "duration": duration,
            "time": datetime.now()
        })

 def session_length(self):
        return (datetime.now() - self.start_time).seconds

    def event_count(self):
        return len(self.events)

    def average_ear(self):
        if not self.events:
            return 0

        total = 0

        for e in self.events:
            total += e["ear"]

        return total / len(self.events)

