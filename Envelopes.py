import math

class Amplitude :

    attackTime = 0
    decayTime = 0
    sustainLevel = 1
    releaseTime = 0

    def __init__(self, _attackTime, _decayTime, _sustainLevel, _releaseTime) :
        self.attackTime = _attackTime
        self.decayTime = _decayTime
        self.sustainLevel = _sustainLevel
        self.releaseTime = _releaseTime

    def SetAttackTime(self, t) :
        self.attackTime = t

    def SetDecayTime(self, t) :
        self.decayTime = t

    def SetSustainLeve(self, lvl) :
        self.sustainLevel = lvl

    def SetReleaseTime(self, t) :
        self.releaseTime = t

    def GetGain(self, t, duration, maxAmp = 1) :
        gain = self.sustainLevel

        if (t < self.attackTime) :
            gain = (maxAmp / 2 * math.sin((math.pi * t / self.attackTime ) - math.pi / 2)) + maxAmp / 2
        elif (t < self.attackTime + self.decayTime) :
            gain = ((maxAmp - self.sustainLevel) / 2 * math.cos((math.pi * (t - self.attackTime) / self.decayTime))) + ((maxAmp + self.sustainLevel) / 2)
        elif (t > duration and t < duration + self.releaseTime) :
            gain = ((self.sustainLevel / 2) * math.cos((math.pi * (t - duration) / self.releaseTime))) + (self.sustainLevel / 2)
        elif (t >= duration + self.releaseTime) :
            gain = 0

        return gain