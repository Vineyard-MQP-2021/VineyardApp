from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore
import datetime
import time
from PyQt5.QtCore import QTimer


# class for main app window, just defines the layout of the app
class MainWindow(QMainWindow):
    switchPage = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./views/mainwindow.ui', self)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        timer = QTimer(self)
        timer.timeout.connect(self.displayDateTime)
        timer.start()
        self.settings.clicked.connect(self.switch)

    def displayDateTime(self):
        self.date.setText(datetime.date.today().strftime("%A %b. %d").upper())
        self.time.setText(time.strftime("%H:%M"))

    def switch(self):
        self.switchPage.emit()
