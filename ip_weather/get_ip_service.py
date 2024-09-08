from exceptions import IPServiceError
from logging import getLogger
import http.client

logger = getLogger(__name__)


def get_ip() -> str:
    """Get ip from external service"""
    try:
        logger.info(f"Запуск модуля {__name__}")
        logger.info("Запрос IP адреса...")
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        ip = conn.getresponse().read().decode()
        logger.info(f"Данные получены, IP адрес: {ip}")
        return ip
    except Exception:
        raise IPServiceError


if __name__ == "__main__":
    print(f"Результат выполнения работы модуля '_get_ip_service': {get_ip()}")
