from coordinates import get_coordinates, Coordinate
from datetime import datetime
from exceptions import ApiServiceError
from enum import Enum
from get_ip_service import get_ip
import json
from json.decoder import JSONDecodeError
import settings
from typing import NamedTuple, Literal
import urllib.request
from urllib.error import URLError

Celsius = float


class WhetherType(Enum):
    Thunderstorm = "Гроза"
    Drizzle = "Морось"
    Rain = "Дождь"
    Snow = "Снег"
    Fog = "Туман"
    Clear = "Ясно"
    Clouds = "Облачно"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WhetherType
    sunrise: datetime
    sunset: datetime
    area: str


def get_weather(coordinates: Coordinate) -> Weather:
    """Эта функция возвращает экземпляр класса Weather при передаче в нее координат"""
    print("Запуск модуля 'weather_api_service'")
    openweather_response = _get_openweather_response(longitude=coordinates.longitude, latitude=coordinates.latitude, API_key=settings.API_key)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(longitude: float, latitude: float, API_key: str) -> str:
    """Эта функция отправляет запрос на сервис openweather"""
    try:
        print("Отправка запроса на сервис погоды")
        url = settings.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude, API_key=API_key)
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError


def _parse_openweather_response(openweather_response: str) -> Weather:
    """Эта функция парсит ответ сервиса погоды"""
    try:
        print("Старт десериализации JSON ответа сервиса погоды")
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError
    print("Старт парсинга ответа сервиса погоды")
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_suntime(openweather_dict, "sunrise"),
        sunset=_parse_suntime(openweather_dict, "sunset"),
        area=_parse_sity(openweather_dict)
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    """Эта функция парсит ответ сервиса погоды для извлечения данных о температуре"""
    print("Старт парсинга температуры")
    return openweather_dict["main"]["temp"]


def _parse_weather_type(openweather_dict: dict) -> WhetherType:
    """Эта функция парсит ответ сервиса погоды для извлечения данных о состоянии погоды"""
    print("Старт парсинга типа погоды")
    try:
                weather_type_id: str = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_type_codes = {
        "800": WhetherType.Clear,
        "80": WhetherType.Clouds,
        "7": WhetherType.Fog,
        "6": WhetherType.Snow,
        "5": WhetherType.Rain,
        "3": WhetherType.Drizzle,
        "2": WhetherType.Thunderstorm,
    }
    for _id, _weather_type in weather_type_codes.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_suntime(openweather_dict: dict, event: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    """Эта функция парсит время восхода/заката солнца"""
    print(f"Старт парсинга времени {event} солнца")
    sun_event_time = datetime.fromtimestamp(openweather_dict["sys"][event])
    return sun_event_time


def _parse_sity(openweather_dict: dict) -> str:
    """Эта функция парсит название местности"""
    print("Старт парсинга названия местности")
    return openweather_dict["name"]


if __name__ == "__main__":
    print(get_weather(get_coordinates(get_ip())))