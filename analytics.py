import csv
import os
from datetime import datetime
from collections import defaultdict
LOG_FILE = "logs/fatigue_events.csv"

class EventLogger:
 def __init__(self):
        self.ensure_log_directory()
        self.ensure_file()
