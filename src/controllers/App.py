import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.PageSwitcher import PageSwitcher
import os
import atexit


class App:

    def __init__(self):
        self.ps = PageSwitcher()
        self.app = QApplication(sys.argv)
        self.ps.showmainwindow()
        atexit.register(self.deleteFiles)
        sys.exit(self.app.exec())

    def deleteFiles(self):
        os.remove("../res/sounds/mourningdove_mod.wav")
        os.remove("../res/sounds/hawk2_mod.wav")
        os.remove("../res/sounds/bird1_mod.wav")
        os.remove("../res/sounds/bird2_mod.wav")


app = App()
