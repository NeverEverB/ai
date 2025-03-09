#!/bin/bash

# Set working directory
cd ~/ai/code

# Fetch the latest script from GitHub
wget -O moonshot_scanner.py "https://raw.githubusercontent.com/brian-ai-dev/moonshot-scanner/main/moonshot_scanner.py"


# Restart the script
pkill -f moonshot_scanner.py
nohup python3 ~/ai/code/moonshot_scanner.py > ~/ai/logs/moonshot_output.log 2>&1 &

echo "Updated and restarted moonshot scanner!"
