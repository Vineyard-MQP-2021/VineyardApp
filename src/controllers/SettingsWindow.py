from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore


class SettingsWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)

        # loads the .ui file for this page of the app
        uic.loadUi('./views/settingswindow.ui', self)
        self.setFixedWidth(1200)
        self.setFixedHeight(1000)

        # this centers the app in the middle of the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def switch(self):
        self.switchPage.emit()
