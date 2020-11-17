import sys
from PyQt5.QtWidgets import QApplication
from src.PageSwitcher import PageSwitcher
from src.models.APIInfo import APIInfo

app = QApplication(sys.argv)
ps = PageSwitcher()
api = APIInfo.getInstance()
ps.showmainwindow()
app.exec()
