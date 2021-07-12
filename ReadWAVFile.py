from os import read
import struct

RIFFChunkBytes = []
fmtSubChunkBytes = []
dataSubChunkBytes = []

chunkID = ""
chunkSize = 0
chunkFormat = ""

subChunk1ID = ""
subChunk1Size = 0
audioFormat = 1
numChannels = 0
sampleRate = 0
byteRate = 0
blockAlign = 0
bitsPerSample = 0

subChunk2ID = ""
subChunk2Size = 0
data = []

def ReadFile(fileName) :
    audioFile = open(fileName, "rb")
    byte = audioFile.read(1)
    pos = 0
    while byte :
        if pos < 12 :
            RIFFChunkBytes.append(byte)
        elif pos < 36 :
            fmtSubChunkBytes.append(byte)
        else :
            dataSubChunkBytes.append(byte)
        pos = pos + 1
        byte = audioFile.read(1)
    __ParseRIFFChunk()
    __ParseFMTSubChunk()
    __ParseDataSubChunk()

    print("Chunk ID : " + chunkID)
    print("Chunk Size : " + str(chunkSize) + " bytes")
    print("Chunk Format : " + chunkFormat)
    print()
    print("Sub Chunk 1 ID : " + subChunk1ID)
    print("Sub Chunk 1 Size : " + str(subChunk1Size) + " bytes")
    print("Audio Format : " + str(audioFormat))
    print("Number of Channels : " + str(numChannels))
    print("Sample Rate : " + str(sampleRate))
    print("Byte Rate : " + str(byteRate))
    print("Block Align : " + str(blockAlign))
    print("Bits per Sample : " + str(bitsPerSample))
    print()
    print("Sub Chunk 2 ID : " + subChunk2ID)
    print("Sub Chunk 2 Size : " + str(subChunk2Size) + " bytes")

def __ParseRIFFChunk() :
    _chunkID = ""
    _chunkSize = None
    _chunkFormat = ""

    const_chunkIDEndPoint = 4
    const_chunkSizeEndPoint = 8
    const_chunkFormatEndPoint = 12

    pos = 0
    for byte in RIFFChunkBytes :
        if pos < const_chunkIDEndPoint :
            _chunkID = _chunkID + byte.decode("utf-8")
        elif pos < const_chunkSizeEndPoint :
            if (_chunkSize == None) :
                _chunkSize = byte
            elif pos < const_chunkFormatEndPoint :
                _chunkSize = _chunkSize + byte
        else :
            _chunkFormat = _chunkFormat + byte.decode("utf-8")
        pos = pos + 1

    global chunkID, chunkSize, chunkFormat
    chunkID = _chunkID
    chunkSize = struct.unpack_from("<I", _chunkSize)[0]
    chunkFormat = _chunkFormat

def __ParseFMTSubChunk() :
    _subChunk1ID = ""
    _subChunk1Size = None
    _audioFormat = None
    _numChannels = None
    _sampleRate = None
    _byteRate = None
    _blockAlign = None
    _bitsPerSample = None

    const_subChunk1IDEndPoint = 4
    const_subChunk1SizeEndPoint = 8
    const_audioFormatEndPoint = 10
    const_numChannelsEndPoint = 12
    const_sampleRateEndPoint = 16
    const_byteRateEndPoint = 20
    const_blockAlignEndPoint = 22
    const_bitsPerSampleEndPoint = 24

    pos = 0
    for byte in fmtSubChunkBytes :
        if pos < const_subChunk1IDEndPoint :
            _subChunk1ID = _subChunk1ID + byte.decode("utf-8")
        elif pos < const_subChunk1SizeEndPoint :
            if _subChunk1Size == None :
                _subChunk1Size = byte
            else :
                _subChunk1Size = _subChunk1Size + byte
        elif pos < const_audioFormatEndPoint :
            if _audioFormat == None :
                _audioFormat = byte
            else :
                _audioFormat = _audioFormat + byte
        elif pos < const_numChannelsEndPoint :
            if _numChannels == None :
                _numChannels = byte
            else :
                _numChannels = _numChannels + byte
        elif pos < const_sampleRateEndPoint :
            if _sampleRate == None :
                _sampleRate = byte
            else :
                _sampleRate = _sampleRate + byte
        elif pos < const_byteRateEndPoint :
            if _byteRate == None :
                _byteRate = byte
            else :
                _byteRate = _byteRate + byte
        elif pos < const_blockAlignEndPoint :
            if _blockAlign == None :
                _blockAlign = byte
            else :
                _blockAlign = _blockAlign + byte
        elif pos < const_bitsPerSampleEndPoint :
            if _bitsPerSample == None :
                _bitsPerSample = byte
            else :
                _bitsPerSample = _bitsPerSample + byte
        pos = pos + 1

    global subChunk1ID, subChunk1Size, audioFormat, numChannels, sampleRate, byteRate, blockAlign, bitsPerSample
    subChunk1ID = _subChunk1ID
    subChunk1Size = struct.unpack_from("<I", _subChunk1Size)[0]
    audioFormat = struct.unpack_from("<H", _audioFormat)[0]
    numChannels = struct.unpack_from("<H", _numChannels)[0]
    sampleRate = struct.unpack_from("<I", _sampleRate)[0]
    byteRate = struct.unpack_from("<I", _byteRate)[0]
    blockAlign = struct.unpack_from("<H", _blockAlign)[0]
    bitsPerSample = struct.unpack_from("<H", _bitsPerSample)[0]

def __ParseDataSubChunk() :
    _subChunk2ID = ""
    _subChunk2Size = None
    _data = []
    dataSample = None

    const_subChunk2IDEndPoint = 4
    const_subChunk2SizeEndPoint = 8
    const_bitsPerByte = 8

    global bitsPerSample
    const_bytesPerSample = bitsPerSample / const_bitsPerByte

    pos = 0
    for byte in dataSubChunkBytes :
        if pos < const_subChunk2IDEndPoint :
            _subChunk2ID = _subChunk2ID + byte.decode("utf-8")
        elif pos < const_subChunk2SizeEndPoint :
            if _subChunk2Size == None :
                _subChunk2Size = byte
            else :
                _subChunk2Size = _subChunk2Size + byte
        else :
            if dataSample == None :
                dataSample = byte
            else : 
                dataSample = dataSample + byte
            if (len(dataSample) == const_bytesPerSample) :
                _data.append(__ParseSample(dataSample))
                dataSample = None
            
        pos = pos + 1

    global subChunk2ID, subChunk2Size, data
    subChunk2ID = _subChunk2ID
    subChunk2Size = struct.unpack_from("<I", _subChunk2Size)[0]
    data = _data

def __ParseSample(sample) :
    result = None
    sampleSize = len(sample)
    if sampleSize == 1 :
        result = ord(sample)
    elif sampleSize == 2 :
        result = struct.unpack_from("<h", sample)[0]
    return result
        
    