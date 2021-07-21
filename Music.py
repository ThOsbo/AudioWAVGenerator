import Instruments

class Sheet :
    sampleRate = 0
    beatsPerMinute = 0
    staves = {}

    def __init__(self, _beatsPerMinute, _sampleRate) :
        self.sampleRate = _sampleRate
        self.beatsPerMinute = _beatsPerMinute

    def AddStave(self, instrument, staveName = None) :
        newStave = Stave(instrument, self.beatsPerMinute, self.sampleRate)
        if staveName == None :
            staveName = str(instrument)
        self.staves[staveName] = newStave

    def GetStave(self, staveName) :
        return self.staves[staveName]

    def GetWave(self, maxAmplitude = 32767) :
        waveToReturn = []
        highestAmp = 0

        for stave in self.staves.values() :
            staveMusic = stave.GetMusic()
            for sampleNum in range(0, len(staveMusic)) :
                if sampleNum >= len(waveToReturn) :
                    waveToReturn.append(staveMusic[sampleNum])
                else :
                    waveToReturn[sampleNum] = waveToReturn[sampleNum] + staveMusic[sampleNum]

                if abs(waveToReturn[sampleNum]) > highestAmp :
                    highestAmp = abs(waveToReturn[sampleNum])
        
        if highestAmp > maxAmplitude :
            condenseFactor = maxAmplitude / highestAmp
            for sampleNum in range(0, len(waveToReturn)) :
                waveToReturn[sampleNum] = condenseFactor * waveToReturn[sampleNum]

        return waveToReturn

class Stave :
    instrument = None
    music = []
    sampleRate = 0
    beatsPerMinute = 0

    def __init__(self, _instrument, _beatsPerMinute, _sampleRate) :
        self.sampleRate = _sampleRate
        self.beatsPerMinute = _beatsPerMinute
        if str(_instrument).lower() == "violin" :
            self.instrument = Instruments.Violin(_sampleRate)
        else :
            raise NotImplementedError

    def AddNote(self, note, beats) :
        duration = (beats / self.beatsPerMinute) * 60   #in seconds
        for sample in self.instrument.GetWave(note, duration) :
            self.music.append(sample)

    def AddBreak(self, beats) :
        duration = (beats / self.beatsPerMinute) * 60   #in seconds
        tStep = 1 / self.sampleRate
        for t in range(0, duration / tStep) :
            self.music.append(0)

    def RepeatStave(self) :
        newStave = []
        for i in range(0, 2) :
            for sample in self.music :
                newStave.append(sample)
        self.music = newStave

    def GetMusic(self) :
        return self.music