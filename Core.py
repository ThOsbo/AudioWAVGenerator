import ByteFiles
import GenerateWave
import Instruments
import Music
import struct

def WriteWaveToFile(wave, sampleRate, fileName) :
    file = open(fileName, "w")

    for i in range(len(wave)) :
        t = i / sampleRate
        file.write(str(t) + "\t\t" + str(wave[i]) + "\n")

    file.close()

if __name__ == "__main__" :

    # drumViolinFile = ByteFiles.wavFile("TestAudio\\TestDrumViolinDuet.wav")

    # testViolin = Instruments.Violin(drumViolinFile.sampleRate)
    # testDrum = Instruments.Drum(drumViolinFile.sampleRate)

    # WriteWaveToFile(testViolin.GetWave("A0", 1), drumViolinFile.sampleRate, "PlotWaves\\TestViolinLowNote.txt")
    # WriteWaveToFile(testDrum.GetWave("A1", 1), drumViolinFile.sampleRate, "PlotWaves\\TestDrumLowNote.txt")

    # musicSheet = Music.Sheet(100, drumViolinFile.sampleRate)
    # musicSheet.AddStave("Violin", "Violin")
    # musicSheet.AddStave("Drum", "Drum", 10)

    # staveViolin = musicSheet.GetStave("Violin")
    # staveViolin.AddNote("E3", 1)
    # staveViolin.AddNote("A440", 1)
    # staveViolin.AddNote("E3", 1)
    # staveViolin.AddNote("A2", 1)

    # staveDrum = musicSheet.GetStave("Drum")
    # staveDrum.AddNote("A1", 1)
    # staveDrum.AddNote("A1", 1)
    # staveDrum.AddNote("A1", 1)
    # staveDrum.AddNote("A1", 1)

    # musicSheetWave = musicSheet.GetWave()

    # drumViolinFile.ClearAudioData()
    # drumViolinFile.AddToAudioData(musicSheetWave)
    # drumViolinFile.WriteFile()
    # drumViolinFile.PrintFile()

    # drumFile = ByteFiles.wavFile("TestAudio\\TestDrum.wav")
    # drumSheet = Music.Sheet(100, drumFile.sampleRate)
    # drumSheet.AddStave("Drum")

    # testDrumStave = drumSheet.GetStave("Drum")
    # testDrumStave.AddNote("A1", 1)
    # testDrumStave.AddNote("C2", 1)
    # testDrumStave.AddNote("D2", 1)
    # testDrumStave.AddNote("F2", 1)
    # testDrumStave.AddNote("G2", 1)
    # testDrumStave.AddNote("B3", 1)
    # testDrumStave.AddNote("E3", 1)

    # testDrumWave = drumSheet.GetWave()
    # WriteWaveToFile(testDrumWave, drumFile.sampleRate, "PlotWaves\\TestDrum.txt")

    # drumFile.ClearAudioData()
    # drumFile.AddToAudioData(testDrumWave)
    # drumFile.WriteFile()
    # drumFile.PrintFile()

    const_h_max = 32767
    const_f_max = struct.unpack_from("<f", b'\xff\xff\x7f\x7f')[0]

    testFile = ByteFiles.wavFile("TestAudio\\TestByteSize.wav")
    testFile.SetBitsPerSample(32)

    testWave = GenerateWave.SquareWave(5, testFile.sampleRate, 100, const_f_max)
    WriteWaveToFile(testWave, testFile.sampleRate, "PlotWaves\\TestByteSize.txt")
    WriteWaveToFile(testFile.data, testFile.sampleRate, "PlotWaves\\TestByteSizeRead.txt")

    testFile.ClearAudioData()
    testFile.AddToAudioData(testWave)
    testFile.WriteFile()
    testFile.PrintFile()