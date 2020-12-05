from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap

from src.models.ZMQMessager import ZMQMessager


class StreamThread(QThread):
    videoSignal = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.zmq = ZMQMessager.getInstance()

    def run(self):
        self.running = True
        while self.running:
            self.zmq.getStream()
            qp = QPixmap()
            qp.loadFromData(self.zmq.frame)
            self.videoSignal.emit(qp)

    def stop(self):
        self.running = False
