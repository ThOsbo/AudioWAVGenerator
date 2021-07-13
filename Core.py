import ByteFiles
import GenerateWave

if __name__ == "__main__" :
    testFileRead = ByteFiles.wavFile("TestAudio\sound.wav")
    testFileRead.PrintFile()
    print("\n")

    testFileWrite = ByteFiles.wavFile("TestAudio\TestFile.wav")
    testFileWrite.WriteFile()
    testFileWrite.PrintFile()
    print("\n")

    testFileWrite2 = ByteFiles.wavFile("TestAudio\TestFile2.wav")
    testFileWrite2.ClearAudioData()
    testFileWrite2.AddToAudioData(GenerateWave.GenerateSquareWave(5, testFileWrite2.sampleRate))
    testFileWrite2.WriteFile()
    testFileWrite2.PrintFile()
    print("\n")