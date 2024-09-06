from exceptions import IPServiceError
import http.client


def get_ip() -> str:
    """Get ip from external service"""
    try:
        print("Запрос IP адреса модулем '_get_ip_service'")
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        return conn.getresponse().read().decode()
    except Exception:
        raise IPServiceError


if __name__ == "__main__":
    print(f"Результат выполнения работы модуля '_get_ip_service': {get_ip()}")
