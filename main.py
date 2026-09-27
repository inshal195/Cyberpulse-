from fastapi import FastAPI
from schemas import IPCheck, URLCheck
from scans.scan_ip import scan_ip
from scans.scan_url import scan_url
from scans.risk_scan import calculate_url_risk

from database import create_tables, save_scan, get_scans


app = FastAPI(
    title="CyberPulse",
    description="Cybersecurity Threat Monitoring and Analysis API",
    version="1.0.0"
)


create_tables()


@app.get("/")
def home():
    return {
        "message": "CyberPulse is alive!",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/about")
def about():
    return {
        "name": "CyberPulse",
        "version": "1.0.0",
        "description": "Cybersecurity threat monitoring and analysis API"
    }


@app.post("/check/ip")
def check_ip(data: IPCheck):

    result = scan_ip(data.ip)

    save_scan(
        "ip",
        data.ip,
        0,
        "informational"
    )

    return result


@app.post("/check/url")
def check_url(data: URLCheck):

    result = scan_url(data.url)

    risk = calculate_url_risk(result)

    if "error" in result:
        return result

    save_scan(
        "url",
        data.url,
        risk["risk_score"],
        risk["risk_level"]
    )

    return {
        "analysis": result,
        "risk": risk
    }


@app.get("/threats")
def threats():

    return {
        "total": len(get_scans()),
        "scans": get_scans()
    }


@app.get("/threats/{scan_id}")
def threat(scan_id: int):

    scans = get_scans()

    for scan in scans:
        if scan["id"] == scan_id:
            return scan

    return {
        "error": "Scan not found"
    }


@app.get("/dashboard")
def dashboard():

    scans = get_scans()

    high = 0
    medium = 0
    low = 0

    for scan in scans:

        if scan["risk_level"] == "high":
            high += 1

        elif scan["risk_level"] == "medium":
            medium += 1

        elif scan["risk_level"] == "low":
            low += 1

    return {
        "total_scans": len(scans),
        "high_risk": high,
        "medium_risk": medium,
        "low_risk": low
    }