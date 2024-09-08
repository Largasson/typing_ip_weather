from exceptions import CoordinateByIpErrorServise
from get_ip_service import get_ip
import json
from logging import getLogger
import settings
from typing import NamedTuple
import urllib.request
from urllib.error import URLError

logger = getLogger(__name__)


class Coordinate(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates(_ip: str) -> Coordinate:
    """Return current coordinates user"""
    logger.info(f"Запуск модуля {__name__}")
    logger.info(f"Запрос координат по IP адресу: {_ip}")
    _ip_coordinate_dict = _ip_coordinate_request(_ip)
    coordinate = Coordinate(
        latitude=round(_ip_coordinate_dict["lat"], 1),
        longitude=round(_ip_coordinate_dict["lon"], 1)
    )
    logger.info(f"Данные получены. По IP адресу {_ip} сервис определяет "
                f"следующие координаты: {coordinate}")
    return coordinate


def _ip_coordinate_request(_ip: str) -> dict:
    """Get JSON from coordinate by IP service and transform to dict"""
    logger.info("Получение дынных в формате JSON")
    url = settings.IP_API_URL.format(query=_ip)
    try:
        return json.loads(urllib.request.urlopen(url).read())
    except URLError:
        raise CoordinateByIpErrorServise


if __name__ == "__main__":
    print(get_coordinates(get_ip()))
