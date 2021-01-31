from PyQt5.QtCore import QThread, pyqtSignal
from src.models.ZMQMessager import ZMQMessager
import time


class ConnectionStatusThread(QThread):
    connectionSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.zmq = ZMQMessager.getInstance()
        self.running = False

    def run(self):
        self.running = True
        while self.running is True:
            time.sleep(0.5)
            s = self.zmq.getConnection()
            self.connectionSignal.emit(s)

    def stop(self):
        self.running = False
