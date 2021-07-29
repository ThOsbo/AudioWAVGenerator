import struct

def ParseRIFFChunk(bytesList) :
    chunkID = ""
    chunkSize = None
    chunkFormat = ""

    const_chunkIDEndPoint = 4
    const_chunkSizeEndPoint = 8
    const_chunkFormatEndPoint = 12

    pos = 0
    for byte in bytesList :
        if pos < const_chunkIDEndPoint :
            chunkID = chunkID + byte.decode("utf-8")
        elif pos < const_chunkSizeEndPoint :
            if (chunkSize == None) :
                chunkSize = byte
            elif pos < const_chunkFormatEndPoint :
                chunkSize = chunkSize + byte
        else :
            chunkFormat = chunkFormat + byte.decode("utf-8")
        pos = pos + 1

    chunkSize = struct.unpack_from("<I", chunkSize)[0]

    return chunkID, chunkSize, chunkFormat

def ParseFMTSubChunk(bytesList) :
    subChunk1ID = ""
    subChunk1Size = None
    audioFormat = None
    numChannels = None
    sampleRate = None
    byteRate = None
    blockAlign = None
    bitsPerSample = None

    const_subChunk1IDEndPoint = 4
    const_subChunk1SizeEndPoint = 8
    const_audioFormatEndPoint = 10
    const_numChannelsEndPoint = 12
    const_sampleRateEndPoint = 16
    const_byteRateEndPoint = 20
    const_blockAlignEndPoint = 22
    const_bitsPerSampleEndPoint = 24

    pos = 0
    for byte in bytesList :
        if pos < const_subChunk1IDEndPoint :
            subChunk1ID = subChunk1ID + byte.decode("utf-8")
        elif pos < const_subChunk1SizeEndPoint :
            if subChunk1Size == None :
                subChunk1Size = byte
            else :
                subChunk1Size = subChunk1Size + byte
        elif pos < const_audioFormatEndPoint :
            if audioFormat == None :
                audioFormat = byte
            else :
                audioFormat = audioFormat + byte
        elif pos < const_numChannelsEndPoint :
            if numChannels == None :
                numChannels = byte
            else :
                numChannels = numChannels + byte
        elif pos < const_sampleRateEndPoint :
            if sampleRate == None :
                sampleRate = byte
            else :
                sampleRate = sampleRate + byte
        elif pos < const_byteRateEndPoint :
            if byteRate == None :
                byteRate = byte
            else :
                byteRate = byteRate + byte
        elif pos < const_blockAlignEndPoint :
            if blockAlign == None :
                blockAlign = byte
            else :
                blockAlign = blockAlign + byte
        elif pos < const_bitsPerSampleEndPoint :
            if bitsPerSample == None :
                bitsPerSample = byte
            else :
                bitsPerSample = bitsPerSample + byte
        pos = pos + 1

    subChunk1Size = struct.unpack_from("<I", subChunk1Size)[0]
    audioFormat = struct.unpack_from("<H", audioFormat)[0]
    numChannels = struct.unpack_from("<H", numChannels)[0]
    sampleRate = struct.unpack_from("<I", sampleRate)[0]
    byteRate = struct.unpack_from("<I", byteRate)[0]
    blockAlign = struct.unpack_from("<H", blockAlign)[0]
    bitsPerSample = struct.unpack_from("<H", bitsPerSample)[0]

    return subChunk1ID, subChunk1Size, audioFormat, numChannels, sampleRate, byteRate, blockAlign, bitsPerSample

def ParseDataSubChunk(bytesList, bytesPerSample) :
    subChunk2ID = ""
    subChunk2Size = None
    data = []
    dataSample = None

    const_subChunk2IDEndPoint = 4
    const_subChunk2SizeEndPoint = 8

    pos = 0
    for byte in bytesList :
        if pos < const_subChunk2IDEndPoint :
            subChunk2ID = subChunk2ID + byte.decode("utf-8")
        elif pos < const_subChunk2SizeEndPoint :
            if subChunk2Size == None :
                subChunk2Size = byte
            else :
                subChunk2Size = subChunk2Size + byte
        else :
            if dataSample == None :
                dataSample = byte
            else : 
                dataSample = dataSample + byte
            if (len(dataSample) == bytesPerSample) :
                data.append(__ParseSample(dataSample))
                dataSample = None
            
        pos = pos + 1

    subChunk2Size = struct.unpack_from("<I", subChunk2Size)[0]

    return subChunk2ID, subChunk2Size, data

def __ParseSample(sample) :
    result = None
    sampleSize = len(sample)
    if sampleSize == 1 :
        result = ord(sample)
    elif sampleSize == 2 :
        result = struct.unpack_from("<h", sample)[0]
    elif sampleSize == 4 :
        result = struct.unpack_from("<f", sample)[0]
    return result
        
    