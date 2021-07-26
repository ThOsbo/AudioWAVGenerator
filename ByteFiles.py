import os
import ParseWAVFileRead
import ParseWAVFileWrite

class wavFile :

    def __init__(self, _filePath) :
        self.chunkID = "RIFF"
        self.chunkSize = 36
        self.chunkFormat = "WAVE"

        self.subChunk1ID = "fmt "
        self.subChunk1Size = 16
        self.audioFormat = 1
        self.numChannels = 1
        self.sampleRate = 44100
        self.bitsPerSample = 16
        self.byteRate = int(self.sampleRate * self.numChannels * self.bitsPerSample / 8)
        self.blockAlign = int(self.numChannels * self.bitsPerSample / 8)

        self.subChunk2ID = "data"
        self.subChunk2Size = 0
        self.data = []

        self.filePath = _filePath
        if os.path.isfile(self.filePath) :
            try :
                self.__ReadFile()
            except :
                pass

    def PrintFile(self) :
        print("Chunk ID : " + self.chunkID)
        print("Chunk Size : " + str(self.chunkSize) + " bytes")
        print("Chunk Format : " + self.chunkFormat)
        print()
        print("Sub Chunk 1 ID : " + self.subChunk1ID)
        print("Sub Chunk 1 Size : " + str(self.subChunk1Size) + " bytes")
        print("Audio Format : " + str(self.audioFormat))
        print("Number of Channels : " + str(self.numChannels))
        print("Sample Rate : " + str(self.sampleRate))
        print("Byte Rate : " + str(self.byteRate))
        print("Block Align : " + str(self.blockAlign))
        print("Bits per Sample : " + str(self.bitsPerSample))
        print()
        print("Sub Chunk 2 ID : " + self.subChunk2ID)
        print("Sub Chunk 2 Size : " + str(self.subChunk2Size) + " bytes")

    def ClearAudioData(self) :
        self.data.clear()
    
    def AddToAudioData(self, samplesToAdd) :
        for sample in samplesToAdd :
            self.data.append(sample)

    def WriteFile(self) :
        self.__SetChunkSizes()
        RIFFChunkBytes = ParseWAVFileWrite.WriteRIFFChunk(self.chunkID, self.chunkSize, self.chunkFormat)
        FmtChunkBytes = ParseWAVFileWrite.WriteFmtChunk(self.subChunk1ID, self.subChunk1Size, self.audioFormat, self.numChannels, self.sampleRate, self.byteRate, self.blockAlign, self.bitsPerSample)
        dataChunkBytes = ParseWAVFileWrite.WriteDataChunk(self.subChunk2ID, self.subChunk2Size, self.data, self.bitsPerSample)        
        file = open(self.filePath, "wb")
        for byte in RIFFChunkBytes :
            file.write(byte)
        for byte in FmtChunkBytes :
            file.write(byte)
        for byte in dataChunkBytes :
            file.write(byte)
        file.close()

    def __SetChunkSizes(self) :
        self.subChunk2Size = int(len(self.data) * self.bitsPerSample / 8)
        self.subChunk1Size = 16
        self.chunkSize = int(4 + 8 + self.subChunk1Size + 8 + self.subChunk2Size)
    
    def __ReadFile(self) :
        RIFFChunkBytes, fmtChunkBytes, dataChunkBytes = self.__SplitFileChunks()

        self.chunkID, self.chunkSize, self.chunkFormat = ParseWAVFileRead.ParseRIFFChunk(RIFFChunkBytes)
        self.subChunk1ID, self.subChunk1Size, self.audioFormat, self.numChannels, self.sampleRate, self.byteRate, self.blockAlign, self.bitsPerSample = ParseWAVFileRead.ParseFMTSubChunk(fmtChunkBytes)
        self.subChunk2ID, self.subChunk2Size, self.data = ParseWAVFileRead.ParseDataSubChunk(dataChunkBytes, self.bitsPerSample)

    def __SplitFileChunks(self) :

        RIFFChunkBytes = []
        fmtSubChunkBytes = []
        dataSubChunkBytes = []

        audioFile = open(self.filePath, "rb")
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
        audioFile.close()

        return RIFFChunkBytes, fmtSubChunkBytes, dataSubChunkBytes