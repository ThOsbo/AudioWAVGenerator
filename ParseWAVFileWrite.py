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

def WriteDataChunk(subChunk2ID, subChunk2Size, data, bytesPerSample) :
    bytesToWrite = []
    bytesToWrite.append(subChunk2ID.encode("utf-8"))
    bytesToWrite.append(struct.pack("<I", int(subChunk2Size)))

    const_h_max = struct.unpack_from("<h", b'\xff\x7f')[0]  #largest little endian short number
    const_f_max = struct.unpack_from("<f", b'\xff\xff\x7f\x7f')[0]  #largest little endian float number

    for val in data :
        if bytesPerSample == 1 :
            if (val > 255) :
                toPack = 255
            elif (val < 0) :
                toPack = 0
            else :
                toPack = val
            byte = bytes([int(toPack)])
        elif bytesPerSample == 2 :
            if (val > const_h_max) :
                toPack = const_h_max
            elif (val < -1 * const_h_max) :
                toPack = -1 * const_h_max
            else :
                toPack = val
            byte = struct.pack("<h", int(toPack))
        elif bytesPerSample == 4 :
            if (val > const_f_max) :
                toPack = const_f_max
            elif (val < -1 * const_f_max) :
                toPack = -1 * const_f_max
            else :
                toPack = val
            toPack = val
            byte = struct.pack("<f", int(toPack))
        bytesToWrite.append(byte)
    return bytesToWrite