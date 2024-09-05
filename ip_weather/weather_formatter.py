from datetime import datetime
from weather_api_service import Weather

time_now = datetime.now()
def format_weather(weather: Weather) -> str:
    """Форматирование данных о погоде в строку"""
    return (f"Погода на {time_now.strftime('%H:%m')} в {weather.area}\n"
            f"{weather.temperature} °С\n"
            f"{weather.weather_type.value}\n"
            f"Восход - {weather.sunrise.strftime('%H:%m')}\n"
            f"Закат  - {weather.sunset.strftime('%H:%m')}"
            )

# if __name__ == "__main__":
#     format_weather()