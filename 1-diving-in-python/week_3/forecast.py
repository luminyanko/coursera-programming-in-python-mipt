import requests
import pprint


class WeatherApi:
    _access_key = 'paste_key_here'

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        print('Sending HTTP request...')
        url = f"http://api.weatherstack.com/forecast?access_key={self._access_key}&query={city}"
        data = requests.get(url).json()
        forecast = {
            "date": data["location"]["localtime"],
            "temp": data["current"]["temperature"]
        }
        self._city_cache[city] = forecast
        return forecast


class CityInfo:
    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or WeatherApi()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    weather_forecast = WeatherApi()
    for _ in range(5):
        city_info = CityInfo("Kharkiv", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)


if __name__ == '__main__':
    _main()
