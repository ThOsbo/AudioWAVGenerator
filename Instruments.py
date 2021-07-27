import math
import GenerateWave
import Filters
import Envelopes

class Violin :

    wave = {"A0" : [], "E1" : [], "A1" : [], "E2" : [], "A2" : [], "E3" : [], "A440" : [], "E4" : [], "A4" : [], "E5" : [], "A5" : [], "E6" : [], "A6" : []}
    duration = {"A0" : 0, "E1" : 0, "A1" : 0, "E2" : 0, "A2" : 0, "E3" : 0, "A440" : 0, "E4" : 0, "A4" : 0, "E5" : 0, "A5" : 0, "E6" : 0, "A6" : 0}
    frequency = {"A0" : 55, "E1" : 82.5, "A1" : 110, "E2" : 165, "A2" : 220, "E3" : 330, "A440" : 440, "E4" : 660, "A4" : 880, "E5" : 1320, "A5" : 1760, "E6" : 2640, "A6" : 3520}

    def __init__(self, _sampleRate) :
        self.sampleRate = _sampleRate
        for note in self.frequency :
            if len(self.wave[note]) == 0 or self.duration[note] == 0 :
                for val in self.__GenerateWave(self.frequency[note], _sampleRate) :
                    self.wave[note].append(val)
                self.duration[note] = len(self.wave[note]) / _sampleRate
    
    def GetWave(self, note, _duration) :
        ampMod = Envelopes.Amplitude((_duration * 8) / 35, (_duration * 5) / 35, 0.7, (_duration * 10) / 35)
        sampleNum = 0

        waveToReturn = []
        numToAdd = _duration // self.duration[note]

        for i in range(0, int(numToAdd)) :
            for val in self.wave[note] :
                t = sampleNum / self.sampleRate
                sampleNum = sampleNum + 1
                waveToReturn.append(val * ampMod.GetGain(t, _duration))
        
        numLeft = _duration - (numToAdd * self.duration[note])

        if (numLeft > 0) :
            extraSamplesToAdd = numLeft * self.sampleRate
            for i in range(0, int(extraSamplesToAdd)) :
                t = sampleNum / self.sampleRate
                sampleNum = sampleNum + 1
                waveToReturn.append(self.wave[note][i] * ampMod.GetGain(t, _duration))

        return waveToReturn

    def __GenerateWave(self, _frequency, _sampleRate) :
        numSamplesSingleWave = _sampleRate // _frequency
        powOf2 = math.ceil(math.log(numSamplesSingleWave, 2))

        _duration = pow(2, powOf2) / _sampleRate
        baseWave = GenerateWave.SawtoothWave(_duration, _sampleRate, _frequency)

        lowPassFilter = Filters.LowPass(10000, 0.5)
        filteredWave = lowPassFilter.FilterWave(baseWave, 1 / _sampleRate)

        return filteredWave[:int(numSamplesSingleWave)]

class Drum :
    wave = {"A1" : [], "C2" : [], "D2" : [], "F2" : [], "G2" : [], "B3" : [], "E3" : []}
    duration = {"A1" : 0, "C2" : 0, "D2" : 0, "F2" : 0, "G2" : 0, "B3" : 0, "E3" : 0}
    frequency = {"A1" : (55, 75), "C2" : (65, 95), "D2" : (75, 110), "F2" : (85, 125), "G2" : (100, 145), "B3" : (120, 175), "E3" : (165, 235)}
    
    def __init__(self, _sampleRate) :
        self.sampleRate = _sampleRate
        for note in self.frequency :
            if len(self.wave[note]) == 0 or self.duration[note] == 0 :
                for val in self.__GenerateWave(self.frequency[note], _sampleRate) :
                    self.wave[note].append(val)
                self.duration[note] = len(self.wave[note]) / _sampleRate
    
    def GetWave(self, note, _duration) :
        ampMod = Envelopes.Amplitude(0.005, 0.5, 0, 0)
        sampleNum = 0

        waveToReturn = []
        numToAdd = _duration // self.duration[note]

        for i in range(0, int(numToAdd)) :
            for val in self.wave[note] :
                t = sampleNum / self.sampleRate
                sampleNum = sampleNum + 1
                waveToReturn.append(val * ampMod.GetGain(t, _duration))
        
        numLeft = _duration - (numToAdd * self.duration[note])

        if (numLeft > 0) :
            extraSamplesToAdd = numLeft * self.sampleRate
            for i in range(0, int(extraSamplesToAdd)) :
                t = sampleNum / self.sampleRate
                sampleNum = sampleNum + 1
                waveToReturn.append(self.wave[note][i] * ampMod.GetGain(t, _duration))

        return waveToReturn

    def __GenerateWave(self, _frequency, _sampleRate) :
        numSamplesSingleWave = _sampleRate
        powOf2 = math.ceil(math.log(numSamplesSingleWave, 2))

        _duration = pow(2, powOf2) / _sampleRate
        baseWave = GenerateWave.Noise(_duration, _sampleRate)

        lowFilter = Filters.LowPass(_frequency[1], 0)
        highFilter = Filters.HighPass(_frequency[0], 0)

        filterWave1 = lowFilter.FilterWave(baseWave, 1 / _sampleRate)
        filterWave2 = highFilter.FilterWave(filterWave1, 1 / _sampleRate)

        highestAbsVal = 0
        for sample in filterWave2 :
            if abs(sample) > highestAbsVal :
                highestAbsVal = abs(sample)
        
        gain =  32767 / highestAbsVal

        waveToReturn = []
        for sample in filterWave2 :
            waveToReturn.append(gain * sample)

        return waveToReturn[:int(numSamplesSingleWave)]