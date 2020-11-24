import librosa
import soundfile as sf
import IPython.display as ipd


class SoundModifier:
    __instance = None
    names = ["mourningdove"]
    pitches = {'mourningdove_pitch': 0, 'hawk2_pitch': 0, 'bird1_pitch': 0, 'bird2_pitch': 0}
    speeds = {'mourningdove_speed': 100, 'hawk2_speed': 100, 'bird1_speed': 100, 'bird2_speed': 100}
    sounds = {'mourningdove': 0}


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

    def applySoundChanges(self):
        for name in self.names:
            url = '../res/sounds/' + name + '.wav'
            self.sounds[name], self.sr = librosa.load(url)
            attr = name + '_speed'
            speed = self.speeds[attr] / 100
            self.sounds[name] = librosa.effects.time_stretch(self.sounds[name], speed)
            attr = name + '_pitch'
            pitch = self.pitches[attr]
            self.sounds[name] = librosa.effects.pitch_shift(self.sounds[name], self.sr, n_steps=pitch)
            new_url = '../res/sounds/' + name + '_mod.wav'
            sf.write(new_url, self.sounds[name], self.sr)


    @staticmethod
    def getInstance():
        if SoundModifier.__instance is None:
            SoundModifier()
        return SoundModifier.__instance
