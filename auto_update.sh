#!/bin/bash

# Define paths
CODE_DIR=~/ai/code
LOG_DIR=~/ai/logs
SCANNER_SCRIPT="$CODE_DIR/moonshot_scanner.py"
TEMP_SCRIPT="$CODE_DIR/moonshot_scanner_temp.py"

# Fetch the latest moonshot_scanner.py from GitHub
echo "Checking for updates..."
wget -q -O "$TEMP_SCRIPT" https://raw.githubusercontent.com/NeverEverB/ai/main/moonshot_scanner.py

# Compare with the existing file
if ! cmp -s "$TEMP_SCRIPT" "$SCANNER_SCRIPT"; then
    mv "$TEMP_SCRIPT" "$SCANNER_SCRIPT"
    chmod +x "$SCANNER_SCRIPT"
    echo "Moonshot Scanner updated! Restarting..."
    
    # Kill existing process
    pkill -f "python3 $SCANNER_SCRIPT"

    # Start fresh
    nohup python3 "$SCANNER_SCRIPT" > "$LOG_DIR/moonshot_output.log" 2>&1 &
    echo "Scanner restarted and running!"
else
    echo "No changes found. Moonshot Scanner is up to date."
    rm "$TEMP_SCRIPT"
fi
