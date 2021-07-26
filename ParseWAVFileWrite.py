import struct

def WriteRIFFChunk(chunkID, chunkSize, chunkFormat) :
    bytesToWrite = []
    bytesToWrite.append(chunkID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", int(chunkSize)))
    bytesToWrite.append(chunkFormat.encode("utf-8"))
    return bytesToWrite

def WriteFmtChunk(subChunk1ID, subChunk1Size, audioFormat, numChannels, sampleRate, byteRate, blockAlign, bitsPerSample) :
    bytesToWrite = []
    bytesToWrite.append(subChunk1ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", int(subChunk1Size)))
    bytesToWrite.append(struct.pack("<H", int(audioFormat)))
    bytesToWrite.append(struct.pack("<H", int(numChannels)))
    bytesToWrite.append(struct.pack("<I", int(sampleRate)))
    bytesToWrite.append(struct.pack("<I", int(byteRate)))
    bytesToWrite.append(struct.pack("<H", int(blockAlign)))
    bytesToWrite.append(struct.pack("<H", int(bitsPerSample)))
    return bytesToWrite

def WriteDataChunk(subChunk2ID, subChunk2Size, data, bitsPerSample) :
    bytesToWrite = []
    bytesToWrite.append(subChunk2ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", int(subChunk2Size)))
    for val in data :
        if bitsPerSample == 8 :
            if (val > 255) :
                toPack = 255
            elif (val < 0) :
                toPack = 0
            else :
                toPack = val
            byte = bytes([int(toPack)])
        elif bitsPerSample == 16 :
            if (val > 32767) :
                toPack = 32767
            elif (val < -32767) :
                toPack = -32767
            else :
                toPack = val
            byte = struct.pack("<h", int(toPack))
        bytesToWrite.append(byte)
    return bytesToWrite