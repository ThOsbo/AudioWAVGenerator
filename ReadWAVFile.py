from os import read
import struct
import sys

RIFFChunkBytes = []
fmtSubChunkBytes = []
dataSubChunkBytes = []

chunkID = ""
chunkSize = 0
chunkFormat = ""

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

    print("Chunk ID : " + chunkID)
    print("Chunk Size : " + str(chunkSize))
    print("Chunk Format : " + chunkFormat)

def __ParseRIFFChunk() :
    pos = 0
    chunkSizeBytes = None
    _chunkID = ""
    _chunkFormat = ""
    for byte in RIFFChunkBytes :
        if pos < 4 :
            _chunkID = _chunkID + byte.decode("utf-8")
        elif pos < 8 :
            if (chunkSizeBytes == None) :
                chunkSizeBytes = byte
            else :
                chunkSizeBytes = chunkSizeBytes + byte
        else :
            _chunkFormat = _chunkFormat + byte.decode("utf-8")
        pos = pos + 1

    global chunkID, chunkSize, chunkFormat
    chunkID = _chunkID
    chunkSize = struct.unpack_from("<I", chunkSizeBytes)[0]
    chunkFormat = _chunkFormat