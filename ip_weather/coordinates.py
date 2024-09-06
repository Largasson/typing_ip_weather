from exceptions import CoordinateByIpErrorServise
from get_ip_service import get_ip
import json
import settings
from typing import NamedTuple
import urllib.request
from urllib.error import URLError


class Coordinate(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates(_ip: str) -> Coordinate:
    """Return current coordinates user"""
    print(f"Запуск модуля 'coordinates' для получения координат по IP адресу: {_ip}")
    _ip_coordinate_dict = _ip_coordinate_request(_ip)
    print("Данные получены")
    return Coordinate(
        latitude=round(_ip_coordinate_dict["lat"], 1),
        longitude=round(_ip_coordinate_dict["lon"], 1)
    )


def _ip_coordinate_request(_ip: str) -> dict:
    """Get JSON from coordinate by IP service and transform to dict"""
    print("Получение дынных в формате JSON")
    url = settings.IP_API_URL.format(query=_ip)
    try:
        return json.loads(urllib.request.urlopen(url).read())
    except URLError:
        raise CoordinateByIpErrorServise


if __name__ == "__main__":
    print(get_coordinates(get_ip()))
