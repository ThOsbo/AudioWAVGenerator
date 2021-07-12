import ReadWAVFile
import WriteWAVFile

if __name__ == "__main__" :
    ReadWAVFile.ReadFile("TestAudio\sound.wav")
    WriteWAVFile.WriteWAVFile()
    print("\n")
    ReadWAVFile.ReadFile("TestAudio\TestFile.wav")