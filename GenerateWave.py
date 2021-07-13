def GenerateSquareWave(duration, sampleRate, frequency = 44100, amplitude = 32767) :
    amplitude = 32767
    frequency = 44100
    offset = 0

    numSamples = int(duration * sampleRate)
    swapSign = int(sampleRate / frequency)
    sign = 1

    waveList = []

    for i in range(numSamples) :
        if (i % swapSign == 0) :
            sign = sign * -1
        val = (sign * amplitude) + offset
        waveList.append(val)

    return waveList