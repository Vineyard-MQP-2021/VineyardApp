from src.controllers.EventWindow import EventWindow
from src.controllers.MainWindow import MainWindow
from src.controllers.SettingsWindow import SettingsWindow


# this class is responsible for all page switching
class PageSwitcher:

    # This constructor does not do anything
    def __init__(self):
        pass

    """this function shows the main window and closes the settings or event window if it exists.
    it also starts the connection status and video stream threads"""

    def showmainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.switchPage.connect(self.switchpage)
        if hasattr(self, "settingswindow"):
            self.settingswindow.close()
        if hasattr(self, "eventwindow"):
            self.eventwindow.close()
        self.mainwindow.show()
        self.mainwindow.videoStream.videoSignal.connect(self.mainwindow.setStream)
        self.mainwindow.connectionThread.connectionSignal.connect(self.mainwindow.setConnection)
        self.mainwindow.videoStream.start()
        self.mainwindow.connectionThread.start()

    # this function shows a specfied secondary window and closes the main window
    def switchpage(self, page):
        if page == "settings":
            self.settingswindow = SettingsWindow()
            self.settingswindow.switchPage.connect(self.showmainwindow)
            self.mainwindow.close()
            self.settingswindow.show()
        else:
            self.eventwindow = EventWindow()
            self.eventwindow.switchPage.connect(self.showmainwindow)
            self.mainwindow.close()
            self.eventwindow.show()
