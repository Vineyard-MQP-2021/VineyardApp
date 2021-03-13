import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.PageSwitcher import PageSwitcher
import os
import atexit


# this class is what launches the app
class App:
    """constructor that creates a page switcher, shows the main window
    registers a function to run at exit"""

    def __init__(self):
        self.ps = PageSwitcher()
        self.app = QApplication(sys.argv)
        self.ps.showmainwindow()
        atexit.register(self.deleteFiles)
        sys.exit(self.app.exec())

    # removes modified sound files on app exit
    def deleteFiles(self):
        os.remove("../res/sounds/hawk1_mod.wav")
        os.remove("../res/sounds/hawk2_mod.wav")
        os.remove("../res/sounds/hawk3_mod.wav")
        os.remove("../res/sounds/hawk4_mod.wav")


app = App()
