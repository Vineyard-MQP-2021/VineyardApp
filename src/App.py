import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

#class for main app window, just defines the layout of the app
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('mainwindow.ui', self)
        self.show()






app = QApplication(sys.argv)
window = MainWindow()
app.exec()