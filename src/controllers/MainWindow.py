from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore, QtGui
import datetime
import time
from PyQt5.QtCore import QTimer

from src.models.APIInfo import APIInfo
from src.res import resources
import astral
from astral import sun


# controller class for main app window
class MainWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal()
    api = APIInfo.getInstance()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # loads the .ui file for this page of the app
        uic.loadUi('./views/mainwindow.ui', self)
        self.setFixedWidth(1200)
        self.setFixedHeight(1000)

        # this centers the app in the center of the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # this works with the displayDataTime function to set the day and time for the app
        timer = QTimer(self)
        timer.timeout.connect(self.displayDateTime)
        timer.start()
        self.setWeather(self.api.weather)
        self.settings.clicked.connect(self.switch)

    def displayDateTime(self):
        self.date.setText(datetime.date.today().strftime("%A %b. %d").upper())
        self.time.setText(time.strftime("%H:%M"))

    thunder = lambda self: self.weather.setPixmap(QPixmap(":/storm"))
    rain = lambda self: self.weather.setPixmap(QPixmap(":/rain"))
    cloud = lambda self: self.weather.setPixmap(QPixmap(":/cloud"))
    snow = lambda self: self.weather.setPixmap(QPixmap(":/snow"))
    clear = lambda self, sunrise, sunset, now: self.weather.setPixmap(QPixmap(":/sun")) if (
            sunrise < now < sunset) else self.weather.setPixmap(QPixmap(":/moon"))
    other_weather = lambda self: self.weather.setPixmap(QPixmap(":/atmosphere"))

    def setWeather(self, weather_code):
        if weather_code == "Clear":
            astral_observer = astral.LocationInfo(timezone=self.api.tz, latitude=self.api.lat, longitude=self.api.lon).observer
            sunrise = sun.sunrise(observer=astral_observer, tzinfo=self.api.tz).time()
            sunset = sun.sunset(observer=astral_observer, tzinfo=self.api.tz).time()
            now = datetime.datetime.now().time()
            self.clear(sunrise, sunset, now)
        else:
            return {
                "Thunderstorm": self.thunder,
                "Rain": self.rain,
                "Drizzle": self.rain,
                "Clouds": self.cloud,
                "Snow": self.snow
            }.get(weather_code, self.other_weather)()


    def switch(self):
        self.switchPage.emit()
