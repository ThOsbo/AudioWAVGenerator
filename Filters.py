import math
import FastFourierTransform

class Filter() :

    cutoffFrequncy = 0
    resonance = 0

    def __init__(self, _cutoffFrequency, _resonance) :
        self.cutoffFrequncy = _cutoffFrequency
        self.resonance = _resonance

    def FilterWave(self, wave, timeStep) :
        fftWave = FastFourierTransform.FFTRecursive(wave)
        freqDomain = FastFourierTransform.GetFrequencyDomain(fftWave, timeStep)
        for i in range(0, len(fftWave)) :
            fftWave[i] = self.__GetGain(freqDomain[i][0]) * fftWave[i]
        filteredWave = FastFourierTransform.inverseFFTRecursive(fftWave)
        toReturn = []
        for complexVal in filteredWave :
            toReturn.append(int(complexVal.real))
        return toReturn
    
    def __GetGain(self, frequency) :
        if (isinstance(self, LowPass)) :
            return self.__LowPassGain(frequency)
        else :
            raise NotImplementedError

    def __LowPassGain(self, frequency) :
        gain = 1        
        startPoint = self.cutoffFrequncy - math.acos(0.707)

        if frequency - startPoint > math.pi / 2 :
            gain = 0
        elif frequency > startPoint :
            gain = math.cos(frequency - startPoint)

        return gain

class LowPass(Filter) :
    pass
