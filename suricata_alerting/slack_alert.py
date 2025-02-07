#!/your/path/to/env/bin/python3
## replace above with your path to your python environment
## FEELING STUCK?? Check out the homelab series on youtube at https://youtube.com/@bowtiedcyberz2h
### OTHER THINGS YOU COULD ADD: error alerting, log storage, time based frequency alerts (ie 100 DNS alerts in 60 seconds)

import os
import time
import traceback
from datetime import datetime, timedelta
from slack_sdk import WebClient #the only external library that needs installing via pip

# CONFIGURATION
FAST_LOG_PATH = "/var/log/suricata/fast.log"
ALERT_LOOKBACK_MINUTES = 2
CHANNEL_ID = "alerts"

# Extract High-Severity Alerts
CRITICAL_ALERT_PATTERNS = [
    "Cobalt Strike",
    "Ransomware",
    "Dshield Block",
    "Poor Reputation IP",
    "Exploit",
    "SQL Injection",
    "Phishing",
    "TOR",
    "Compromised Host",
    "Remote Code Execution",
    "Brute Force Attack",
    "Shellcode",
    "Trojan",
    "Command and Control",
    "APT-",
    "Malware",
    "Worm",
    "CoinMiner",
    "CVE"]


def send_alert(message): #doesn't reutrn anything because it's meant to be run as a daemon but it could
    with open("token.txt", "r") as file:
        SLACK_BOT_TOKEN = file.read().strip()  # Strip removes extra spaces or new lines
    client = WebClient(token=SLACK_BOT_TOKEN)
    response = client.chat_postMessage(channel=CHANNEL_ID, text=message)


def parse_suricata_log():
    """Parse the Suricata fast.log file and check for critical alerts in the last 2 minutes."""
    if not os.path.exists(FAST_LOG_PATH):
        print(f"[!] Log file {FAST_LOG_PATH} not found!")
        return #this one we actually need to return something because it ends the function if the fastlog isn't found

    now = datetime.now()
    time_threshold = now - timedelta(minutes=ALERT_LOOKBACK_MINUTES)
    alerts_found = []

    with open(FAST_LOG_PATH, "r") as f:
        for line in f:
            parts = line.split(" ", 1)
            timestamp_str = parts[0].split('.')[0]
            try:
                log_time = datetime.strptime(timestamp_str, "%m/%d/%Y-%H:%M:%S")
                if log_time >= time_threshold and any(rule in line for rule in CRITICAL_ALERT_PATTERNS):
                    alerts_found.append(line.strip())
            except ValueError:
                print(traceback.print_exc())  # Skip lines that don’t match expected timestamp format
                continue

    if alerts_found:
        alert_message = "\n".join(alerts_found)
        send_alert(alert_message)

if __name__ == "__main__":
    while True:
        try:
            parse_suricata_log()
            time.sleep(60)
        except:
            print(traceback.print_exc())
            time.sleep(60)
