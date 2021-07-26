import math
import random

def Noise(duration, sampleRate, amplitude = 32767) :
    t0 = 0
    tN = duration
    tStep = 1 / sampleRate

    waveList = []

    for i in range(t0, int(tN / tStep)) :
        waveList.append(random.randint(int(-amplitude), int(amplitude)))

    return waveList

def SinWave(duration, sampleRate, frequency, amplitude = 32767) :
    t0 = 0
    tN = duration
    tStep = 1 / sampleRate

    waveList = []

    for i in range(t0, int(tN / tStep)) :
        t = t0 + (i * tStep)
        waveList.append(amplitude * math.sin(2 * math.pi * frequency * t))

    return waveList

def SquareWave(duration, sampleRate, frequency, amplitude = 32767) :
    numSamples = int(duration * sampleRate)
    swapSign = int(sampleRate / frequency)      #in number of samples
    sign = 1

    waveList = []

    for i in range(numSamples) :
        x = i % (swapSign / 2)
        if (x == 0 and i != 0) :
            sign = sign * -1
        val = (sign * amplitude)
        waveList.append(val)

    return waveList

def SawtoothWave(duration, sampleRate, frequency, amplitude = 32767) :
    #also known as a ramp wave
    numSamples = int(duration * sampleRate)
    waveLength = int(sampleRate / frequency)    #in number of samples
    gradient = 2 * amplitude / waveLength

    waveList = []

    for i in range(numSamples) :
        val = int(gradient * (i % waveLength)) - amplitude
        waveList.append(val)

    return waveList   


def TriangleWave(duration, sampleRate, frequency, amplitude = 32767) :
    numSamples = int(duration * sampleRate)
    waveLength = int(sampleRate / frequency)    #in number of samples
    gradient = 4 * amplitude / waveLength
    sign = 1
    c = 0

    waveList = []

    for i in range(numSamples) :
        x = (i % (waveLength / 2))
        if x == 0 and i != 0 :
            sign = sign * -1

        if sign == 1 :
            c = -amplitude
        else :
            c = amplitude
        
        val = int(c + (sign * gradient) * x)

        waveList.append(val)

    return waveList 