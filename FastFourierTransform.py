import math
import cmath

def FFTRecursive(a) :

    a = __SetLenToPower2(a)

    i = cmath.sqrt(-1)
    n = len(a)
    if n == 1 :
        return a
    nOmega = cmath.exp(2 * cmath.pi * i / n)
    omega = 1

    a0 = []
    a1 = []
    for index in range(0, len(a)) :
        if index % 2 == 0 :
            a0.append(a[index])
        else :
            a1.append(a[index])
    y0 = FFTRecursive(a0)
    y1 = FFTRecursive(a1)

    y = []
    for index in range(0, n) :
        y.append(0)

    for k in range(0, int(n/2)) :
        y[k] = y0[k] + omega * y1[k]
        y[k + int(n/2)] = y0[k] - omega * y1[k]
        omega = omega * nOmega
    
    return y

def inverseFFTRecursive(y) :
    y = __SetLenToPower2(y)

    i = cmath.sqrt(-1)
    n = len(y)
    if n == 1 :
        return y
    nOmega = cmath.exp(-2 * cmath.pi * i / n)
    omega = 1

    y0 = []
    y1 = []
    for index in range(0, len(y)) :
        if index % 2 == 0 :
            y0.append(y[index])
        else :
            y1.append(y[index])
    a0 = FFTRecursive(y0)
    a1 = FFTRecursive(y1)

    a = []
    for index in range(0, n) :
        a.append(0)

    for k in range(0, int(n/2)) :
        a[k] = (a0[k] + omega * a1[k]) / n
        a[k + int(n/2)] = (a0[k] - omega * a1[k]) / n
        omega = omega * nOmega
    
    return a

def GetFrequencyDomain(fourierTransform, timeStep) :
    fN = 1 / timeStep
    N = len(fourierTransform)
    freqDomain = []
    for i in range(0, N) :
        freq = i * fN / N
        freqDomain.append((freq, abs(fourierTransform[i])))
    return freqDomain

def GetTimeDomain(invFourierTransform, timeStep, t0 = 0) :
    N = len(invFourierTransform)
    timeDomain = []
    for i in range(0, N) :
        t = t0 + i * timeStep
        timeDomain.append((t, invFourierTransform[i].real))
    return timeDomain

def __SetLenToPower2(listToAdjust) :
    power = math.ceil(math.log(len(listToAdjust), 2))
    while (len(listToAdjust) < pow(2, power)) :
        listToAdjust.append(0)
    return listToAdjust