import Instruments

class Sheet :
    sampleRate = 0
    beatsPerMinute = 0
    staves = {}

    def __init__(self, _beatsPerMinute, _sampleRate) :
        self.sampleRate = _sampleRate
        self.beatsPerMinute = _beatsPerMinute

    def AddStave(self, instrument) :
        newStave = Stave(instrument, self.beatsPerMinute, self.sampleRate)
        self.staves[instrument] = newStave

class Stave :
    instrument = None
    music = []
    sampleRate = 0
    beatsPerMinute = 0

    def __init__(self, _instrument, _beatsPerMinute, _sampleRate) :
        self.sampleRate = _sampleRate
        self.beatsPerMinute = _beatsPerMinute
        if str(_instrument).lower() == "Violin" :
            self.instrument = Instruments.Violin(_sampleRate)
        else :
            raise NotImplementedError

    def AddNote(self, note, beats) :
        duration = (beats / self.beatsPerMinute) / 60   #in seconds
        for sample in self.instrument.GetWave(note, duration) :
            self.music.append(sample)

    def AddBreak(self, beats) :
        duration = (beats / self.beatsPerMinute) / 60   #in seconds
        tStep = 1 / self.sampleRate
        for t in range(0, duration / tStep) :
            self.music.append(0)

    def RepeatStave(self) :
        newStave = []
        for i in range(0, 2) :
            for sample in self.music :
                newStave.append(sample)
        self.music = newStave