def calculate_url_risk(scan_result: dict) -> dict:

    if "error" in scan_result:
        return {
            "risk_score": 0,
            "risk_level": "invalid",
            "warnings": ["Invalid URL"]
        }

    score = 0
    warnings = []

    if not scan_result["is_https"]:
        score += 20
        warnings.append("URL does not use HTTPS")

    if scan_result["has_ip_hostname"]:
        score += 25
        warnings.append("Hostname is an IP address")

    if scan_result["has_at_symbol"]:
        score += 25
        warnings.append("URL contains @ symbol")

    if scan_result["url_length"] > 100:
        score += 10
        warnings.append("URL is unusually long")

    if score >= 50:
        risk_level = "high"
    elif score >= 25:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "risk_score": min(score, 100),
        "risk_level": risk_level,
        "warnings": warnings
    }