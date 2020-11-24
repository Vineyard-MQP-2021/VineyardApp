import json
import socket
import requests
from src import api_keys

"""this class serves as a singleton. This is so the app only has to call the two apis once per app launch.
This class saves the info for whenever the user returns to the main page!"""


class APIInfo:
    __instance = None

    def __init__(self):
        if APIInfo.__instance is not None:
            raise Exception("Error")
        else:
            APIInfo.__instance = self
            self.getipinfo()
            self.getweatherinfo()

    def getipinfo(self):
        # In order to get the approximate user's location, their ip address is used
        # The ipinfo (https://ipinfo.io/) api is used to find approximate latitude and longitude from ip address.
        ip = socket.gethostbyname(socket.gethostname())
        ip_url = "http://ipinfo.io/" + ip
        ip_params = {'token': api_keys.ipAPIKey}
        ip_api_response = requests.get(url=ip_url, params=ip_params).text
        try:
            ip_response_data = json.loads(ip_api_response)
            self.lat = ip_response_data["loc"].split(",")[0]
            self.lon = ip_response_data["loc"].split(",")[1]
            self.tz = ip_response_data["timezone"]
        except KeyError:
            self.bogon = True
            print("An error occurred!")

    def getweatherinfo(self):
        # The latitude and longitude from the ipinfo api is used to find the current weather
        # the openweathermap (http://api.openweathermap.org/data/2.5/weather) api is used
        if self.bogon is not True:
            weather_url = "http://api.openweathermap.org/data/2.5/weather"
            weather_params = {'lat': self.lat, 'lon': self.lon, 'units': "imperial", "appid": api_keys.weatherAPIKey}
            weather_api_response = requests.get(url=weather_url, params=weather_params).text
            try:
                weather_response_data = json.loads(weather_api_response)
                self.weather = weather_response_data["weather"][0]["main"]
                self.temp = round(weather_response_data["main"]["temp"])
            except ValueError:
                print("An error occurred")

    @staticmethod
    def getInstance():
        if APIInfo.__instance is None:
            APIInfo()
        return APIInfo.__instance
