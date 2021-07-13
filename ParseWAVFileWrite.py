import struct

def WriteRIFFChunk(chunkID, chunkSize, chunkFormat) :
    bytesToWrite = []
    bytesToWrite.append(chunkID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", chunkSize))
    bytesToWrite.append(chunkFormat.encode("utf-8"))
    return bytesToWrite

def WriteFmtChunk(subChunk1ID, subChunk1Size, audioFormat, numChannels, sampleRate, byteRate, blockAlign, bitsPerSample) :
    bytesToWrite = []
    bytesToWrite.append(subChunk1ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", subChunk1Size))
    bytesToWrite.append(struct.pack("<H", audioFormat))
    bytesToWrite.append(struct.pack("<H", numChannels))
    bytesToWrite.append(struct.pack("<I", sampleRate))
    bytesToWrite.append(struct.pack("<I", byteRate))
    bytesToWrite.append(struct.pack("<H", blockAlign))
    bytesToWrite.append(struct.pack("<H", bitsPerSample))
    return bytesToWrite

def WriteDataChunk(subChunk2ID, subChunk2Size, data, bitsPerSample) :
    bytesToWrite = []
    bytesToWrite.append(subChunk2ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", subChunk2Size))
    for val in data :
        if bitsPerSample == 8 :
            byte = bytes([val])
        elif bitsPerSample == 16 :
            byte = struct.pack("<h", val)
        bytesToWrite.append(byte)
    return bytesToWrite