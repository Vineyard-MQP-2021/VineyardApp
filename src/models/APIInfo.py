import json
import requests
from src import api_keys

"""this class serves as a singleton. This is so the app only has to call the two APIs once per app launch.
This class saves the info for whenever the user returns to the main page!"""


class APIInfo:
    __instance = None

    # this constructor ensures that it doesn't create another insance if not needed
    def __init__(self):
        if APIInfo.__instance is not None:
            raise Exception("Error")
        else:
            APIInfo.__instance = self
            self.getipinfo()
            self.getweatherinfo()

    # this function calls the ipinfo API to retrieve the user's lat and lon from their ip
    def getipinfo(self):
        # In order to get the approximate user's location, their ip address is used
        # The ipinfo (https://ipinfo.io/) api is used to find approximate latitude and longitude from ip address.
        get_ip = {'format': 'json'}
        ip_addr = requests.get(url="https://api.ipify.org/", params=get_ip).text
        ip = json.loads(ip_addr)['ip']
        ip_url = "http://ipinfo.io/" + ip
        ip_params = {'token': api_keys.ipAPIKey}
        ip_api_response = requests.get(url=ip_url, params=ip_params).text
        try:
            ip_response_data = json.loads(ip_api_response)
            self.lat = ip_response_data["loc"].split(",")[0]
            self.lon = ip_response_data["loc"].split(",")[1]
            self.tz = ip_response_data["timezone"]
        except KeyError:
            print("An error occurred!")

    # this function gets the current weather
    def getweatherinfo(self):
        # The latitude and longitude from the ipinfo api is used to find the current weather
        # the openweathermap (http://api.openweathermap.org/data/2.5/weather) api is used
        weather_url = "http://api.openweathermap.org/data/2.5/weather"
        weather_params = {'lat': self.lat, 'lon': self.lon, 'units': "imperial", "appid": api_keys.weatherAPIKey}
        weather_api_response = requests.get(url=weather_url, params=weather_params).text
        try:
            weather_response_data = json.loads(weather_api_response)
            self.weather = weather_response_data["weather"][0]["main"]
            self.temp = round(weather_response_data["main"]["temp"])
        except ValueError:
            print("An error occurred")

    # this function creates a new instance if needed, and returns an instance of APIInfo
    @staticmethod
    def getInstance():
        if APIInfo.__instance is None:
            APIInfo()
        return APIInfo.__instance
