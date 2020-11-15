from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore, QtGui
import datetime
import time
from PyQt5.QtCore import QTimer

# controller class for main app window


class MainWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal()

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
        self.setWeather("Thunderstorm")

    def displayDateTime(self):
        self.date.setText(datetime.date.today().strftime("%A %b. %d").upper())
        self.time.setText(time.strftime("%H:%M"))

    def setWeather(self, weather_code):
        if weather_code == "Thunderstorm":
            print("thunder")
        elif weather_code == "Rain" or "Drizzle":
            print("rain")
        elif weather_code == "Clear":
            print("clear")
        elif weather_code == "Snow":
            print("snow")
        elif weather_code == "Clouds":
            print("clouds")
        else:
            print("other")

    def switch(self):
        self.switchPage.emit()
