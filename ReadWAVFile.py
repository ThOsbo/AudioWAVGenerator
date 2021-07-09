from os import read
import struct
import sys

RIFFChunkBytes = []
fmtSubChunkBytes = []
dataSubChunkBytes = []

chunkID = ""
chunkSize = 0
chunkFormat = ""

subChunk1ID = ""
subChunk1Size = 0
audioFormat = ""
numChannels = 0
sampleRate = 0
byteRate = 0
blockAlign = 0
bitsPerSample = 0

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

    print("Chunk ID : " + chunkID)
    print("Chunk Size : " + str(chunkSize))
    print("Chunk Format : " + chunkFormat)
    print()
    print("Sub Chunk 1 ID : " + subChunk1ID)
    print("Sub Chunk 1 Size : " + str(subChunk1Size))
    print("Audio Format : " + str(audioFormat))
    print("Number of Channels : " + str(numChannels))
    print("Sample Rate : " + str(sampleRate))
    print("Byte Rate : " + str(byteRate))
    print("Block Align : " + str(blockAlign))
    print("Bits per Sample : " + str(bitsPerSample))
    print()

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
    