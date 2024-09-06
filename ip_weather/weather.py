from coordinates import get_coordinates
from get_ip_service import get_ip
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    print("Запуск программы")
    ip = get_ip()
    coordinates = get_coordinates(ip)
    print(f"Координаты:{coordinates.latitude},{coordinates.longitude}")
    weather = get_weather(coordinates)
    format_weather(weather)
    print("Окончание работы программы")


if __name__ == "__main__":
    main()
