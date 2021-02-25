from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QTableWidgetItem, QLabel, QMessageBox, QHeaderView
from PyQt5 import uic, QtCore
from pymongo import MongoClient
import base64

from src.res import resources
from src import api_keys


class EventWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(EventWindow, self).__init__(*args, **kwargs)

        # loads the .ui file for this page of the app
        uic.loadUi('../views/eventwindow.ui', self)
        self.setFixedWidth(1300)
        self.setFixedHeight(1250)
        self.imageDict = {}

        # this centers the app in the middle of the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.back.clicked.connect(self.switch)
        self.event_table.horizontalHeader().setStretchLastSection(True)
        self.event_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.event_table.setItem(0, 0, QTableWidgetItem("Date"))
        self.event_table.setItem(0, 1, QTableWidgetItem("Time"))
        self.event_table.cellClicked.connect(lambda: self.cellClicked())
        self.refresh.clicked.connect(lambda: self.refreshPage())
        self.refreshPage()

    def cellClicked(self):
        row = self.event_table.currentRow()
        if row in self.imageDict:
            self.showModal(self.imageDict[row])

    def showModal(self, b64):
        byteString = base64.b64decode(b64)
        box = QMessageBox()
        pic = QLabel()
        qp = QPixmap()
        qp.loadFromData(byteString)
        pic.setPixmap(qp)
        box.setIconPixmap(qp)
        box.setWindowTitle("This image was captured!")
        box.exec_()

    def refreshPage(self):
        self.event_table.setRowCount(1)
        client = MongoClient(api_keys.mongodb)
        db = client['Motion']
        collection = db['detections']
        for x in collection.find():
            rowPosition = self.event_table.rowCount()
            self.event_table.insertRow(rowPosition)
            self.event_table.setItem(rowPosition, 0, QTableWidgetItem(x['date']))
            self.event_table.setItem(rowPosition, 1, QTableWidgetItem(x['time']))
            self.imageDict[rowPosition] = x['b64']

    def switch(self):
        self.switchPage.emit()
