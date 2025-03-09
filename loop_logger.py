import os
import time
import subprocess
from datetime import datetime

# Define folder paths
BASE_DIR = os.path.expanduser("~/ai")
LOG_DIR = os.path.join(BASE_DIR, "logs")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def run_command():
    """Runs a test command and logs output."""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = os.path.join(LOG_DIR, f"log_{timestamp}.txt")

    command = "echo 'This is a test command running at '$(date)"  # Fix variable expansion

    
    with open(log_file, "w") as f:
        process = subprocess.Popen(command, shell=True, stdout=f, stderr=f)
        process.communicate()
    
    print(f"Log saved to {log_file}")

def take_screenshot():
    """Captures a screenshot and saves it."""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file = os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png")
    
    command = f"scrot '{screenshot_file}'"
    subprocess.run(command, shell=True)
    
    print(f"Screenshot saved to {screenshot_file}")

while True:
    run_command()
    take_screenshot()
    time.sleep(30)
