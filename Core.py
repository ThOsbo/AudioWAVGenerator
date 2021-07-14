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

    testSquareFile = ByteFiles.wavFile("TestAudio\SquareWave.wav")
    testSquareFile.ClearAudioData()
    testSquareFile.AddToAudioData(GenerateWave.SquareWave(5, testSquareFile.sampleRate, 500))
    testSquareFile.WriteFile()
    testSquareFile.PrintFile()
    print("\n")

    testSawtoothFile = ByteFiles.wavFile("TestAudio\SawtoothWave.wav")
    testSawtoothFile.ClearAudioData()
    testSawtoothFile.AddToAudioData(GenerateWave.SawtoothWave(5, testSawtoothFile.sampleRate, 500))
    testSawtoothFile.WriteFile()
    testSawtoothFile.PrintFile()
    print("\n")

    testTriangleFile = ByteFiles.wavFile("TestAudio\TriangleWave.wav")
    testTriangleFile.ClearAudioData()
    testTriangleFile.AddToAudioData(GenerateWave.TriangleWave(5, testTriangleFile.sampleRate, 500))
    testTriangleFile.WriteFile()
    testTriangleFile.PrintFile()
    print("\n")