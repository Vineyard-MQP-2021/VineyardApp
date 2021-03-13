import librosa
import soundfile as sf


# this class is used to modify the sound files as the user specifies
class SoundModifier:
    __instance = None
    pitches = {'hawk1_pitch': 0, 'hawk2_pitch': 0, 'hawk3_pitch': 0, 'hawk4_pitch': 0}
    speeds = {'hawk1_speed': 100, 'hawk2_speed': 100, 'hawk3_speed': 100, 'hawk4_speed': 100}

    # this constructor ensures that it doesn't create another insance if not needed
    def __init__(self):
        if SoundModifier.__instance is not None:
            raise Exception("Error")
        else:
            SoundModifier.__instance = self

    """this function runs whenever the pitch slider moves.
    it stores the pitch for modifying"""

    def changePitch(self, val, name):
        attr = name + '_pitch'
        self.pitches[attr] = val

    """this function runs whenever the speed slider moves.
    it stores the speed for modifying"""

    def changeSpeed(self, val, name):
        attr = name + '_speed'
        self.speeds[attr] = val

    """this function applies the changes to speed and pitch
    and creates a new sound file"""

    def applySoundChanges(self, name):
        url = '../res/sounds/' + name + '.wav'
        self.sound, self.sampling_rate = librosa.load(url)
        attr = name + '_speed'
        speed = self.speeds[attr] / 100
        self.sound = librosa.effects.time_stretch(self.sound, speed)
        attr = name + '_pitch'
        pitch = self.pitches[attr]
        self.sound = librosa.effects.pitch_shift(self.sound, self.sampling_rate, n_steps=pitch)
        new_url = '../res/sounds/' + name + '_mod.wav'
        sf.write(new_url, self.sound, self.sampling_rate)

    # this function creates a new instance if needed, and returns an instance of SoundModifier
    @staticmethod
    def getInstance():
        if SoundModifier.__instance is None:
            SoundModifier()
        return SoundModifier.__instance
