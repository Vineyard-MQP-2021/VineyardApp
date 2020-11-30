from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore

from src.models.SoundModifier import SoundModifier
from src.res import resources

class EventWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(EventWindow, self).__init__(*args, **kwargs)

        # loads the .ui file for this page of the app
        uic.loadUi('../views/eventwindow.ui', self)
        self.setFixedWidth(1200)
        self.setFixedHeight(1200)

        # this centers the app in the middle of the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.back.clicked.connect(self.switch)

    def switch(self):
        self.switchPage.emit()
