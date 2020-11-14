import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import datetime
import time
from PyQt5.QtCore import QTimer


# class for main app window, just defines the layout of the app
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setFixedHeight(1000)
        self.setFixedWidth(1200)
        uic.loadUi('mainwindow.ui', self)
        timer = QTimer(self)
        timer.timeout.connect(self.displayDateTime)
        timer.start()

    def displayDateTime(self):
        self.date.setText(datetime.date.today().strftime("%A %b. %d").upper())
        self.time.setText(time.strftime("%H:%M"))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
