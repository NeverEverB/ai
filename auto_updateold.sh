#!/bin/bash

# Set working directory
cd ~/ai/code

# Fetch the latest script from GitHub
wget -O ~/ai/code/moonshot_scanner.py https://raw.githubusercontent.com/NeverEverB/ai/main/moonshot_scanner.py


# Restart the script
pkill -f moonshot_scanner.py
nohup python3 ~/ai/code/moonshot_scanner.py > ~/ai/logs/moonshot_output.log 2>&1 &

echo "Updated and restarted moonshot scanner!"
