from exceptions import IPServiceError

import http.client


def get_ip() -> str:
    """Get ip from external servise"""
    try:
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        return conn.getresponse().read().decode()
    except Exception:
        raise IPServiceError


if __name__ == "__main__":
    get_ip()
