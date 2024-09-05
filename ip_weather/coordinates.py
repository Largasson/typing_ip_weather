from exceptions import CoordinateByIpErrorServise
from get_ip_servise import get_ip
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
    _ip_coordinate_dict = _ip_coordinate_request(_ip)
    return Coordinate(
        latitude=round(_ip_coordinate_dict["lat"],1),
        longitude=round(_ip_coordinate_dict["lon"],1)
    )


def _ip_coordinate_request(_ip: str) -> dict:
    """Get JSON from coordinate by IP servise and transform to dict"""
    url = settings.IP_API_URL.format(query=_ip)
    try:
        return json.loads(urllib.request.urlopen(url).read())
    except URLError:
        raise CoordinateByIpErrorServise


if __name__ == "__main__":
    get_coordinates(get_ip())
