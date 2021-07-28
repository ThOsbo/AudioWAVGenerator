import Instruments

class Sheet :
    def __init__(self, _beatsPerMinute, _sampleRate) :
        self.sampleRate = _sampleRate
        self.beatsPerMinute = _beatsPerMinute
        self.staves = {}

    def AddStave(self, instrument, staveName = None, numInstruments = 1) :
        if staveName == None :
            staveName = str(instrument)
        self.staves[staveName] = Stave(instrument, self.beatsPerMinute, self.sampleRate, numInstruments)

    def GetStave(self, staveName) :
        return self.staves[staveName]

    def GetWave(self, maxAmplitude = 32767) :
        waveToReturn = []
        highestAmp = 0

        for stave in self.staves.values() :
            staveMusic = stave.GetMusic()
            for instrumentNum in range(0, stave.numInstruments) :
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
    def __init__(self, _instrument, _beatsPerMinute, _sampleRate, _numInstruments = 1) :
        self.music = []
        self.sampleRate = _sampleRate
        self.beatsPerMinute = _beatsPerMinute
        self.numInstruments = _numInstruments
        if str(_instrument).lower() == "violin" :
            self.instrument = Instruments.Violin(_sampleRate)
        elif str(_instrument).lower() == "drum" :
            self.instrument = Instruments.Drum(_sampleRate)
        else :
            raise NotImplementedError

    def AddNote(self, note, beats) :
        duration = (beats / self.beatsPerMinute) * 60   #in seconds
        for sample in self.instrument.GetWave(note, duration) :
            self.music.append(sample)

    def AddBreak(self, beats) :
        duration = (beats / self.beatsPerMinute) * 60   #in seconds
        tStep = 1 / self.sampleRate
        for t in range(0, int(duration / tStep)) :
            self.music.append(0)

    def RepeatStave(self) :
        newStave = []
        for i in range(0, 2) :
            for sample in self.music :
                newStave.append(sample)
        self.music = newStave

    def GetMusic(self) :
        return self.music