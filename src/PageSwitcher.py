from src.controllers.MainWindow import MainWindow
from src.controllers.SettingsWindow import SettingsWindow


class PageSwitcher:
    def __init__(self):
        pass

    def showmainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.switchPage.connect(self.showsettingswindow)
        if hasattr(self, "settingswindow"):
            self.settingswindow.close()
        self.mainwindow.show()

    def showsettingswindow(self):
        self.settingswindow = SettingsWindow()
        self.settingswindow.switchPage.connect(self.showmainwindow)
        self.mainwindow.close()
        self.settingswindow.show()
