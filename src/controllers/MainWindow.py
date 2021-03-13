from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore
import datetime
import time
from PyQt5.QtCore import QTimer

from src.models.APIInfo import APIInfo
from src.models.ConnectionStatusThread import ConnectionStatusThread
from src.models.StreamThread import StreamThread
from src.models.ZMQMessager import ZMQMessager
from src.res import resources
import astral
from astral import sun


# controller class for main app window

class MainWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal(str)

    api = APIInfo.getInstance()
    videoStream = StreamThread()
    connectionThread = ConnectionStatusThread()

    """This is the constructor that hooks up functionality to
    all of the buttons and sets the current weather"""

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # loads the .ui file for this page of the app
        uic.loadUi('../views/mainwindow.ui', self)
        self.setFixedWidth(1300)
        self.setFixedHeight(1250)

        # this centers the app in the center of the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # this works with the displayDataTime function to set the day and time for the app
        timer = QTimer(self)
        timer.timeout.connect(self.displayDateTime)
        timer.start()
        self.setWeather(self.api.weather)
        self.settings.clicked.connect(lambda: self.switch("settings"))
        self.event.clicked.connect(lambda: self.switch("event"))
        self.hawk1.clicked.connect(lambda: self.sendSound("hawk1"))
        self.hawk2.clicked.connect(lambda: self.sendSound("hawk2"))
        self.hawk3.clicked.connect(lambda: self.sendSound("hawk3"))
        self.hawk4.clicked.connect(lambda: self.sendSound("hawk4"))

    # this function sets the correct date and time on the page
    def displayDateTime(self):
        self.date.setText(datetime.date.today().strftime("%A %b. %d").upper())
        self.time.setText(time.strftime("%H:%M"))

    # these are lambda functions that set the correct weather icon depending on the current weather
    thunder = lambda self: self.weather.setPixmap(QPixmap(":/storm"))
    rain = lambda self: self.weather.setPixmap(QPixmap(":/rain"))
    cloud = lambda self: self.weather.setPixmap(QPixmap(":/cloud"))
    snow = lambda self: self.weather.setPixmap(QPixmap(":/snow"))
    clear = lambda self, sunrise, sunset, now: self.weather.setPixmap(QPixmap(":/sun")) if (
            sunrise < now < sunset) else self.weather.setPixmap(QPixmap(":/moon"))
    other_weather = lambda self: self.weather.setPixmap(QPixmap(":/atmosphere"))

    """this function uses the weather lambdas to compare the weather API info to the lambda
    values and set the weather accordingly"""

    def setWeather(self, weather_code):
        self.temp.setText(str(self.api.temp) + '\u00b0 F')
        if weather_code == "Clear":
            astral_observer = astral.LocationInfo(timezone=self.api.tz, latitude=self.api.lat,
                                                  longitude=self.api.lon).observer
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

    # this function switches the page and stops the connection status and video stream threads
    def switch(self, page):
        self.videoStream.stop()
        self.connectionThread.stop()
        self.switchPage.emit(page)

    # this function sets the stream to the newest received stream frame
    def setStream(self, qp):
        self.video.setPixmap(qp)

    # this function sets the connection status to the latest receieved connection status
    def setConnection(self, s):
        if s == 'c':
            self.connectionstatus.setStyleSheet("color:green;")
            self.connectionstatus.setText("Connected!")
        else:
            self.connectionstatus.setStyleSheet("color:red;")
            self.connectionstatus.setText("Not Connected!")
            self.video.setPixmap(QPixmap(":/vineyard"))

    # this function sends modified sound files to the Raspberry Pi when the buttons are pressed
    def sendSound(self, sound):
        zmq = ZMQMessager.getInstance()
        zmq.sendAudio(sound)
