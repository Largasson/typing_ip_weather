from coordinates import get_coordinates
from get_ip_service import get_ip
from logging import getLogger, basicConfig, DEBUG
from weather_api_service import get_weather
from weather_formatter import format_weather

FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
logger = getLogger("Weather")
basicConfig(level=DEBUG, format=FORMAT)


def main():
    logger.info("Запуск программы")
    ip = get_ip()
    coordinates = get_coordinates(ip)
    weather = get_weather(coordinates)
    format_weather(weather)
    logger.info("Окончание работы программы")


if __name__ == "__main__":
    main()
