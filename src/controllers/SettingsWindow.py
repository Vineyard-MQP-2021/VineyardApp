from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore


class SettingsWindow(QMainWindow):
    switchPage = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./views/settingswindow.ui', self)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def switch(self):
        self.switchPage.emit()
