import math
import FastFourierTransform

class Filter() :

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
        elif (isinstance(self, HighPass)) :
            return self.__HighPassGain(frequency)
        elif (isinstance(self, Notch)) :
            return self.__NotchGain(frequency)
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

    def __HighPassGain(self, frequency) :
        gain = 0
        startPoint = self.cutoffFrequncy - math.asin(0.707)

        if frequency - startPoint > math.pi / 2 :
            gain = 1
        elif frequency > startPoint :
            gain = math.sin(frequency - startPoint)

        return gain

    def __NotchGain(self, frequency) :
        gain = 1

        if frequency < self.cutoffFrequncy :
            startPoint = self.cutoffFrequncy - math.acos(0.707)

            if frequency - startPoint > math.pi / 2 :
                gain = 0
            elif frequency > startPoint :
                gain = math.cos(frequency - startPoint)      

        else :
            startPoint = self.cutoffFrequncy - math.asin(0.707)

            if frequency - startPoint > math.pi / 2 :
                gain = 1
            elif frequency > startPoint :
                gain = math.sin(frequency - startPoint)

        return gain

class LowPass(Filter) :
    pass

class HighPass(Filter) :
    pass

class Notch(Filter) :
    pass
