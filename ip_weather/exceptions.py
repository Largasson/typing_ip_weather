class CantGetCoordinate(Exception):
    """Program can't get GPS coordinate"""


class ApiServiceError(Exception):
    """Program can't get current weather """


class IPServiceError(Exception):
    """Program can't get ip"""


class CoordinateByIpErrorServise(Exception):
    """Program can't get coordinate by IP"""
