import librosa
import soundfile as sf


class SoundModifier:
    __instance = None
    pitches = {'mourningdove_pitch': 0, 'hawk2_pitch': 0, 'bird1_pitch': 0, 'bird2_pitch': 0}
    speeds = {'mourningdove_speed': 100, 'hawk2_speed': 100, 'bird1_speed': 100, 'bird2_speed': 100}

    def __init__(self):
        if SoundModifier.__instance is not None:
            raise Exception("Error")
        else:
            SoundModifier.__instance = self

    def changePitch(self, val, objName):
        attr = objName + '_pitch'
        self.pitches[attr] = val

    def changeSpeed(self, val, objName):
        attr = objName + '_speed'
        self.speeds[attr] = val

    def applySoundChanges(self, name):
        url = '../res/sounds/' + name + '.wav'
        self.sound, self.sr = librosa.load(url)
        attr = name + '_speed'
        speed = self.speeds[attr] / 100
        self.sound = librosa.effects.time_stretch(self.sound, speed)
        attr = name + '_pitch'
        pitch = self.pitches[attr]
        self.sound = librosa.effects.pitch_shift(self.sound, self.sr, n_steps=pitch)
        new_url = '../res/sounds/' + name + '_mod.wav'
        sf.write(new_url, self.sound, self.sr)

    @staticmethod
    def getInstance():
        if SoundModifier.__instance is None:
            SoundModifier()
        return SoundModifier.__instance
