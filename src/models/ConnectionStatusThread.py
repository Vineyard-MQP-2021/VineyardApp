from PyQt5.QtCore import QThread, pyqtSignal
from src.models.ZMQMessager import ZMQMessager
import time

"""this class is used to always maintain the connection status between the app and the pi.
A separate thread is needed so the App's UI does not lock up!"""


class ConnectionStatusThread(QThread):
    connectionSignal = pyqtSignal(str)

    # this constructor fetches the ZMQMessager singleton
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.zmq = ZMQMessager.getInstance()
        self.running = False

    """this function runs as long as the app is open. It gets the connection
    status every 0.5 seconds"""

    def run(self):
        self.running = True
        while self.running is True:
            time.sleep(0.5)
            s = self.zmq.getConnection()
            self.connectionSignal.emit(s)

    # this function stops the thread
    def stop(self):
        self.running = False
