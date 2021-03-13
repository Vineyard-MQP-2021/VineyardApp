from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap

from src.models.ZMQMessager import ZMQMessager

"""this class is used to always maintain the live stream feed between the app and the pi.
A separate thread is needed so the App's UI does not lock up!"""


class StreamThread(QThread):
    videoSignal = pyqtSignal(QPixmap)

    # this constructor fetches the ZMQMessager singleton
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.zmq = ZMQMessager.getInstance()

    """this function runs as long as the app is open. It
    continually gets the live stream feed frame by frame"""

    def run(self):
        self.running = True
        while self.running:
            self.zmq.getStream()
            qp = QPixmap()
            qp.loadFromData(self.zmq.frame)
            self.videoSignal.emit(qp)

    # this function stops the thread
    def stop(self):
        self.running = False
