# Suricata Alert Monitor  

## Requirements.txt

It's so small that I'm just gonna tell you to do this instead of making a whole file for ONE package:

pip install slack_sdk

Into your local python env

## Overview  

This project is a monitoring script designed to analyze Suricata logs and detect high-severity security alerts. It continuously scans the Suricata **fast.log** file for specific threat indicators and sends notifications when critical threats are detected.  

## Features  

- Monitors **fast.log** for high-severity security threats  
- Identifies patterns related to **ransomware, malware, brute force attacks, and exploits**  
- Sends **real-time alerts** to a designated Slack channel  
- Runs on a scheduled interval to check for new alerts  
- Supports configurable log paths and alert lookback windows  

## How It Works  

1. The script reads from the Suricata **fast.log** file.  
2. It looks for alerts that occurred within the past **two minutes**.  
3. If any alerts match predefined high-risk patterns, they are collected.  
4. The script sends an alert message to a **Slack channel** with the details of the detected threats.  
5. The script continuously runs in a loop, checking for new alerts every minute.  

## Alert Categories  

The script identifies and sends alerts for:  

- **Intrusion attempts** (e.g., **remote code execution, shellcode, Trojans**)  
- **Compromised hosts** (e.g., **command and control activity, malware infections**)  
- **Network-based threats** (e.g., **DShield blocklists, TOR connections, poor reputation IPs**)  
- **Exploits and vulnerabilities** (e.g., **SQL injection, CVE-based detections**)  

## Configuration  

- **Log Path**: The location of the Suricata **fast.log** file is set in the script.  
- **Alert Lookback Time**: The script checks for alerts within a configurable time window.  
- **Slack Integration**: Requires a **Slack bot token** stored in a local file to send alerts.  

## Use Case  

This script is useful for **SOC teams, security analysts, and network administrators** who need **real-time notifications** for high-priority security threats detected by Suricata. It enhances incident response by providing immediate visibility into potential attacks.  

## Disclaimer  

This script is provided **as-is** without warranty. It should be tested in a controlled environment before deployment in production.  

## NEED HELP??

Check out the homelab series on youtube at https://youtube.com/@bowtiedcyberz2h to see how it works and how we built it!
