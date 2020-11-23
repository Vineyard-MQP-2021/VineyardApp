import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.PageSwitcher import PageSwitcher
from src.models.APIInfo import APIInfo
import os
import atexit

def deleteFiles():
    os.remove("../res/sounds/mourningdove_mod.wav")
    os.remove("../res/sounds/hawk2_mod.wav")
    os.remove("../res/sounds/bird1_mod.wav")
    os.remove("../res/sounds/bird2_mod.wav")


app = QApplication(sys.argv)
ps = PageSwitcher()
api = APIInfo.getInstance()
ps.showmainwindow()
atexit.register(deleteFiles)
sys.exit(app.exec())
