from urllib.parse import urlparse
import ipaddress


def scan_url(url: str) -> dict:

    parsed_url = urlparse(url)

    if not parsed_url.scheme or not parsed_url.hostname:
        return {
            "error": "Invalid URL"
        }

    hostname = parsed_url.hostname

    try:
        ipaddress.ip_address(hostname)
        has_ip_hostname = True
    except ValueError:
        has_ip_hostname = False

    return {
        "url": url,
        "scheme": parsed_url.scheme,
        "hostname": hostname,
        "port": parsed_url.port,
        "path": parsed_url.path,
        "query": parsed_url.query,
        "is_https": parsed_url.scheme.lower() == "https",
        "has_ip_hostname": has_ip_hostname,
        "has_at_symbol": "@" in url,
        "url_length": len(url)
    }