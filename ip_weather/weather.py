from coordinates import get_coordinates
from get_ip_service import get_ip
from logging import getLogger, basicConfig, DEBUG, ERROR, FileHandler, StreamHandler
from weather_api_service import get_weather
from weather_formatter import format_weather

logger = getLogger("Weather")
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
file_handler = FileHandler("data.log", 'w', encoding='utf-8')
file_handler.setLevel(DEBUG)
console = StreamHandler()
console.setLevel(ERROR)
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])



def main():
    logger.error("Запуск программы")
    ip = get_ip()
    coordinates = get_coordinates(ip)
    weather = get_weather(coordinates)
    format_weather(weather)
    logger.info("Окончание работы программы")


if __name__ == "__main__":
    main()
