import requests
import time
import json
from datetime import datetime

# DexScreener API endpoint
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/search?q=new"

# Log file for detected tokens
LOG_FILE = "~/ai/logs/moonshot_tokens.json"

# Detection Criteria
MIN_VOLUME = 5000  # Minimum trading volume
MAX_MARKET_CAP = 1000000  # Low-cap for moonshot potential
MIN_LIQUIDITY = 10000  # Ensures enough backing


def fetch_new_tokens():
    """Fetches new trading pairs from DexScreener."""
    try:
        response = requests.get(DEXSCREENER_API)
        data = response.json()
        return data.get("pairs", [])
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []


def filter_moonshots(pairs):
    """Filters out potential moonshots based on volume, market cap, and liquidity."""
    moonshots = []
    for pair in pairs:
        try:
            volume = float(pair["volume"].get("h24", 0))  # 24-hour volume
            liquidity = float(pair.get("liquidity", 0))
            market_cap = float(pair.get("fdv", 0))  # Fully diluted valuation (market cap)

            if volume > MIN_VOLUME and market_cap < MAX_MARKET_CAP and liquidity > MIN_LIQUIDITY:
                moonshots.append(pair)
        except Exception as e:
            print(f"Error processing pair: {e}")
    return moonshots


def save_to_log(moonshots):
    """Saves detected moonshots to a log file."""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    data = {"timestamp": timestamp, "moonshots": moonshots}
    
    with open(LOG_FILE, "a") as f:
        json.dump(data, f, indent=4)
    print(f"{len(moonshots)} moonshots logged at {timestamp}")


if __name__ == "__main__":
    while True:
        print("Scanning for moonshots...")
        new_tokens = fetch_new_tokens()
        moonshots = filter_moonshots(new_tokens)
        if moonshots:
            save_to_log(moonshots)
        time.sleep(60)  # Scan every 60 seconds

