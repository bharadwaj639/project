import csv
from datetime import datetime

def log_usage(username, role, action):
    with open("docs/usage_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, role, action, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
