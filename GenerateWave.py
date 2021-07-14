def SquareWave(duration, sampleRate, frequency = 44100, amplitude = 32767, offset = 0) :
    numSamples = int(duration * sampleRate)
    swapSign = int(sampleRate / frequency)      #in number of samples
    sign = 1

    waveList = []

    for i in range(numSamples) :
        x = i % (swapSign / 2)
        if (x == 0 and i != 0) :
            sign = sign * -1
        val = (sign * amplitude) + offset
        waveList.append(val)

    return waveList

def SawtoothWave(duration, sampleRate, frequency = 44100, amplitude = 32767, offset = 0) :
    #also known as a ramp wave
    numSamples = int(duration * sampleRate)
    waveLength = int(sampleRate / frequency)    #in number of samples
    gradient = amplitude / waveLength

    waveList = []

    for i in range(numSamples) :
        val = int(gradient * (i % waveLength)) + offset
        waveList.append(val)

    return waveList   


def TriangleWave(duration, sampleRate, frequency = 44100, amplitude = 32767, offset = 0) :
    numSamples = int(duration * sampleRate)
    waveLength = int(sampleRate / frequency)    #in number of samples
    gradient = 2 * amplitude / waveLength
    sign = 1
    c = 0

    waveList = []

    for i in range(numSamples) :
        x = (i % (waveLength / 2))
        if x == 0 and i != 0 :
            sign = sign * -1

        if sign == 1 :
            c = 0
        else :
            c = amplitude
        
        val = int(c + (sign * gradient) * x)

        waveList.append(val)


    return waveList 