import sys
from PyQt5.QtWidgets import QApplication
from src.PageSwitcher import PageSwitcher

app = QApplication(sys.argv)
ps = PageSwitcher()
ps.showmainwindow()
app.exec()
