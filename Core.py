import ByteFiles
import GenerateWave
import Instruments
import Envelopes

def WriteWaveToFile(wave, sampleRate, fileName) :
    file = open(fileName, "w")

    for i in range(len(wave)) :
        t = i / sampleRate
        file.write(str(t) + "\t\t" + str(wave[i]) + "\n")

    file.close()

if __name__ == "__main__" :

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
    
