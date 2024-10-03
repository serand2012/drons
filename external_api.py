import requests


# Интеграция с внешним API

#Класс WeatherAPI отвечает за взаимодействие с API для получения данных о погоде.
class WeatherAPI:
    def __init__(self, api_key):

        #Инициализация API с ключом доступа.
        #:param api_key: Ключ доступа к API

        self.api_key = api_key

    def get_weather(self, location):

        #Получает данные о погоде для указанного местоположения.
        #:param location: Название местоположения (город, страна)
        #:return: Погодные условия и скорость ветра

        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={location}"
        response = requests.get(url)
        data = response.json()
        return data['current']['condition']['text'], data['current']['wind_mph']


    #Пример использования WeatherAPI
    #weather_api = WeatherAPI(api_key='МОЙ-АПИ-КЛЮЧ')
    #weather_conditions, wind_speed = weather_api.get_weather('New York')
    #print(f"Current weather: {weather_conditions}, Wind speed: {wind_speed} mph")

