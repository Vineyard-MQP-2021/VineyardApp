from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore

from src.models.SoundModifier import SoundModifier
from src.res import resources


class SettingsWindow(QMainWindow):
    # signal used for switching pages
    switchPage = QtCore.pyqtSignal()
    soundModifier = SoundModifier.getInstance()

    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)

        # loads the .ui file for this page of the app
        uic.loadUi('../views/settingswindow.ui', self)
        self.setFixedWidth(1200)
        self.setFixedHeight(1200)

        # this centers the app in the middle of the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.back.clicked.connect(self.switch)
        self.pitch.valueChanged.connect(self.update)
        self.speed.valueChanged.connect(self.update)
        self.soundsettingsbuttons.buttonClicked[int].connect(self.enableSliders)

    def switch(self):
        self.soundModifier.applySoundChanges()
        self.switchPage.emit()

    def update(self, value):
        if value > 10:
            self.speedlabel.setText(str(value))
            self.soundModifier.changeSpeed(value, self.currentButton)
        else:
            self.pitchlabel.setText(str(value))
            self.soundModifier.changePitch(value, self.currentButton)

    def enableSliders(self, id):
        for b in self.soundsettingsbuttons.buttons():
            if b is self.soundsettingsbuttons.button(id):
                self.currentButton = self.soundsettingsbuttons.button(id).objectName()
                b.setStyleSheet("background-color: rgb(85, 164, 165); border: 3px solid #1d54a3; border-radius: 35px;")
                self.pitch.setValue(self.soundModifier.pitches[self.currentButton + '_pitch'])
                self.speed.setValue(self.soundModifier.speeds[self.currentButton + '_speed'])
                self.pitch.setEnabled(True)
                self.speed.setEnabled(True)
            else:
                b.setStyleSheet("background-color: rgb(85, 164, 165);border: none;border-radius: 35px;")
