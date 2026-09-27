import ipaddress
import socket
import asyncio

def scan_ip(ip: str):
    try:
        IP = ipaddress.ip_address(ip)

        hostname = None
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except (socket.herror, socket.gaierror):
            pass

        return {
            "ip": ip,
            "status": "private" if IP.is_private else "public",
            "version": IP.version,
            "private": IP.is_private,
            "is_loopback": IP.is_loopback,
            "is_global": IP.is_global,
            "is_multicast": IP.is_multicast,
            "is_unspecified": IP.is_unspecified,
            "hostname": hostname
        }

    except ValueError:
        return {
            "error": "not valid IP"
        }




