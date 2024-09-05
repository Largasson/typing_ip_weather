from coordinates import get_coordinates
from get_ip_servise import get_ip
from weather_api_service import get_weather
from weather_formatter import format_weather

text = 'test text for scv'

"""Вносим изменения для тестирования SCV"""

"""Продолжаем вносить изменения"""

def main():
    ip = get_ip()
    coordinates = get_coordinates(ip)
    print(f"Координаты:{coordinates.latitude},{coordinates.longitude}")
    weather = get_weather(coordinates)
    print(format_weather(weather))


if __name__ == "__main__":
    main()
