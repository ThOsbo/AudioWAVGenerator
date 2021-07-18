import ByteFiles
import GenerateWave
import Filters
import Instruments

def WriteWaveToFile(wave, sampleRate, fileName) :
    file = open(fileName, "w")

    for i in range(len(wave)) :
        t = i / sampleRate
        file.write(str(t) + "\t\t" + str(wave[i]) + "\n")

    file.close()

if __name__ == "__main__" :
    # testFileRead = ByteFiles.wavFile("TestAudio\sound.wav")
    # testFileRead.PrintFile()
    # print("\n")

    # testFileWrite = ByteFiles.wavFile("TestAudio\TestFile.wav")
    # testFileWrite.WriteFile()
    # testFileWrite.PrintFile()
    # print("\n")

    # testSquareFile = ByteFiles.wavFile("TestAudio\SquareWave.wav")
    # testSquareFile.ClearAudioData()
    # testSquareFile.AddToAudioData(GenerateWave.SquareWave(5, testSquareFile.sampleRate, 500))
    # testSquareFile.WriteFile()
    # testSquareFile.PrintFile()
    # print("\n")

    # testSawtoothFile = ByteFiles.wavFile("TestAudio\SawtoothWave.wav")
    # testSawtoothFile.ClearAudioData()
    # testSawtoothFile.AddToAudioData(GenerateWave.SawtoothWave(5, testSawtoothFile.sampleRate, 500))
    # testSawtoothFile.WriteFile()
    # testSawtoothFile.PrintFile()
    # print("\n")

    # testTriangleFile = ByteFiles.wavFile("TestAudio\TriangleWave.wav")
    # testTriangleFile.ClearAudioData()
    # testTriangleFile.AddToAudioData(GenerateWave.TriangleWave(5, testTriangleFile.sampleRate, 500))
    # testTriangleFile.WriteFile()
    # testTriangleFile.PrintFile()
    # print("\n")

    # testSynthesis = ByteFiles.wavFile("TestAudio\SynthesisSawWave.wav")
    # filter = Filters.LowPass(500, 0.5)
    # testSynthesis.ClearAudioData()
    # sawtoothWave = GenerateWave.SawtoothWave(5, testSynthesis.sampleRate, 250, 5000)
    # filteredWave = filter.FilterWave(sawtoothWave, testSynthesis.sampleRate)
    # WriteWaveToFile(sawtoothWave, testSynthesis.sampleRate, "PlotWaves\ToFilterSawWave.txt")
    # WriteWaveToFile(filteredWave, testSynthesis.sampleRate, "PlotWaves\FilteredSawWave.txt")
    # testSynthesis.AddToAudioData(filteredWave)
    # testSynthesis.WriteFile()
    # testSynthesis.PrintFile()

    duration = 2
    frequency = 440
    testViolin = ByteFiles.wavFile("TestAudio\TestViolinWave.wav")
    baseWave = GenerateWave.SawtoothWave(duration, testViolin.sampleRate, frequency)
    WriteWaveToFile(baseWave, testViolin.sampleRate, "PlotWaves\BaseSawtoothWave.txt")
    tempViolin = Instruments.Violin(testViolin.sampleRate)
    notes = ["A0", "E1", "A1", "E2", "A2", "E3", "A440", "E4", "A4", "E5", "A5", "E6", "A6"]
    testViolin.ClearAudioData()
    for note in notes :
        tempViolinWave = tempViolin.GetWave(note, duration)
        WriteWaveToFile(tempViolinWave, testViolin.sampleRate, "PlotWaves\ViolinTest" + note + "Wave.txt")
        testViolin.AddToAudioData(tempViolinWave)
    testViolin.WriteFile()
    testViolin.PrintFile()
    
