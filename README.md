# CyberPulse

CyberPulse is a cybersecurity threat analysis API built with Python and FastAPI

It analyzes IP and URL and give safe score based on their characteristics, it check parameters like (http,hostname,port,path and more)

## Features

- IP address analysis
- Private/public IP detection
- IP version detection
- Loopback, multicast, global and unspecified IP detection
- Reverse DNS hostname lookup
- URL structure analysis
- HTTPS detection
- IP-based hostname detection
- Suspicious @ symbol detection
- URL length analysis
- Basic URL risk scoring
- SQLite scan history
- Threat history API
- Risk dashboard

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn

## Project Structure

```text
CyberPulse/
│
├── main.py
├── database.py
├── schemas.py
│
├── scans/
│   ├── scan_ip.py
│   ├── scan_url.py
│   └── risk_scan.py
│
├── requirements.txt
├── README.md
