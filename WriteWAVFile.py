import struct

chunkID = "RIFF"
chunkSize = 36
chunkFormat = "WAVE"

subChunk1ID = "fmt "
subChunk1Size = 16
audioFormat = 1
numChannels = 1
sampleRate = 44100
bitsPerSample = 16
byteRate = int(sampleRate * numChannels * bitsPerSample / 8)
blockAlign = int(numChannels * bitsPerSample / 8)

subChunk2ID = "data"
subChunk2Size = 0
data = []

bytesToWrite = []

def WriteWAVFile() :
    filePath = "TestAudio\TestFile.wav"

    GenerateSquareWave(10)
    SetChunkSizes()

    WriteRIFFChunk()
    WriteFmtChunk()
    WriteDataChunk()

    file = open(filePath, "wb")

    global bytesToWrite

    for byte in bytesToWrite :
        file.write(byte)

    for byte in data :
        file.write(byte)
    
    file.close()

def WriteRIFFChunk() :
    global chunkID, chunkSize, chunkFormat, bytesToWrite

    bytesToWrite.append(chunkID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", chunkSize))
    bytesToWrite.append(chunkFormat.encode("utf-8"))

def WriteFmtChunk() :
    global subChunk1ID, subChunk1Size, audioFormat, numChannels, sampleRate, bitsPerSample, byteRate, blockAlign, bytesToWrite

    bytesToWrite.append(subChunk1ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", subChunk1Size))
    bytesToWrite.append(struct.pack("<H", audioFormat))
    bytesToWrite.append(struct.pack("<H", numChannels))
    bytesToWrite.append(struct.pack("<I", sampleRate))
    bytesToWrite.append(struct.pack("<I", byteRate))
    bytesToWrite.append(struct.pack("<H", blockAlign))
    bytesToWrite.append(struct.pack("<H", bitsPerSample))

def WriteDataChunk() :
    global subChunk2ID, subChunk2Size, bytesToWrite

    bytesToWrite.append(subChunk2ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", subChunk2Size))

def GenerateSquareWave(duration) :
    global data, byteRate, bitsPerSample
    amplitude = 32767
    frequency = 44100
    offset = 0

    numBytes = int(duration * byteRate)
    swapSign = int(byteRate / frequency)
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

def SetChunkSizes() :
    global data, subChunk2Size, subChunk1Size, chunkSize

    subChunk2Size = int(len(data))
    subChunk1Size = 16
    chunkSize = int(4 + 8 + subChunk1Size + 8 + subChunk2Size)