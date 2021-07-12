from os import write
import struct

chunkID = "RIFF"
chunkSize = 0
chunkFormat = "WAVE"

subChunk1ID = "fmt"
subChunk1Size = 16
audioFormat = 1
numChannels = 1
sampleRate = 44100
bitsPerSample = 16
byteRate = sampleRate * numChannels * bitsPerSample / 8
blockAlign = numChannels * bitsPerSample / 8

subChunk2ID = "data"
subChunk2Size = 0
data = []

def WriteRIFFChunk() :
    pass

def WriteFmtChunk() :
    pass

def WriteDataChunk() :
    pass

def GenerateSquareWave(duration) :
    global data, byteRate, bitsPerSample
    amplitude = 32767
    frequency = 1
    offset = 0

    numBytes = duration * byteRate
    swapSign = byteRate / frequency
    sign = 1

    for i in range(numBytes) :
        if (i % swapSign == 0) :
            sign = sign * -1
        val = (sign * amplitude) + offset
        if bitsPerSample == 8 :
            byte = bytes([val])
        elif bitsPerSample == 16 :
            byte = struct.pack("<h", val)
        data.append(byte)