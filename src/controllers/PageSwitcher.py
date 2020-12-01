from src.controllers.EventWindow import EventWindow
from src.controllers.MainWindow import MainWindow
from src.controllers.SettingsWindow import SettingsWindow


class PageSwitcher:
    def __init__(self):
        pass

    # this function shows the main window and closes the settings window if it exists
    def showmainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.switchPage.connect(self.switchpage)
        if hasattr(self, "settingswindow"):
            self.settingswindow.close()
        if hasattr(self, "eventwindow"):
            self.eventwindow.close()
        self.mainwindow.show()

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
