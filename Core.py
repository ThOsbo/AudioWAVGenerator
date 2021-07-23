import ByteFiles
import GenerateWave
import Instruments
import Music

def WriteWaveToFile(wave, sampleRate, fileName) :
    file = open(fileName, "w")

    for i in range(len(wave)) :
        t = i / sampleRate
        file.write(str(t) + "\t\t" + str(wave[i]) + "\n")

    file.close()

if __name__ == "__main__" :

    # duration = 2
    # frequency = 440
    # testViolin = ByteFiles.wavFile("TestAudio\TestViolinWave.wav")
    # baseWave = GenerateWave.SawtoothWave(duration, testViolin.sampleRate, frequency)
    # WriteWaveToFile(baseWave, testViolin.sampleRate, "PlotWaves\BaseSawtoothWave.txt")
    # tempViolin = Instruments.Violin(testViolin.sampleRate)
    # notes = ["A0", "E1", "A1", "E2", "A2", "E3", "A440", "E4", "A4", "E5", "A5", "E6", "A6"]
    # testViolin.ClearAudioData()
    # for note in notes :
    #     tempViolinWave = tempViolin.GetWave(note, duration)
    #     WriteWaveToFile(tempViolinWave, testViolin.sampleRate, "PlotWaves\ViolinTest" + note + "Wave.txt")
    #     testViolin.AddToAudioData(tempViolinWave)
    # testViolin.WriteFile()
    # testViolin.PrintFile()

    # beatsPerMinute = 100
    # testMusicFile = ByteFiles.wavFile("TestAudio\TestMusicScore.wav")
    # MusicSheet = Music.Sheet(beatsPerMinute, testMusicFile.sampleRate)
    # MusicSheet.AddStave("Violin")
    
    # violinStave = MusicSheet.GetStave("Violin")
    # violinStave.AddNote("A440", 4)
    # violinStave.AddNote("E3", 1)
    # violinStave.AddNote("A2", 1)
    # violinStave.AddNote("E3", 0.5)
    # violinStave.AddNote("A440", 0.5)
    # violinStave.AddNote("E4", 1)
    # violinStave.AddNote("A440", 4)

    # musicSheetWave = MusicSheet.GetWave()
    # WriteWaveToFile(musicSheetWave, testMusicFile.sampleRate, "PlotWaves\TestMusicWave.txt")

    # testMusicFile.ClearAudioData()
    # testMusicFile.AddToAudioData(musicSheetWave)
    # testMusicFile.WriteFile()
    # testMusicFile.PrintFile()

    beatsPerMinute = 100
    testMusicFile = ByteFiles.wavFile("TestAudio\TestMusicDuetScore.wav")
    MusicSheet = Music.Sheet(beatsPerMinute, testMusicFile.sampleRate)
    MusicSheet.AddStave("Violin", "Violin1")
    MusicSheet.AddStave("Violin", "Violin2")
    
    violinStave = MusicSheet.GetStave("Violin1")
    violinStave.AddNote("A440", 4)
    violinStave.AddNote("E3", 1)
    violinStave.AddNote("A2", 1)
    violinStave.AddNote("E3", 0.5)
    violinStave.AddNote("A440", 0.5)
    violinStave.AddNote("E4", 1)
    violinStave.AddNote("A440", 4)

    violinStave2 = MusicSheet.GetStave("Violin2")
    violinStave2.AddBreak(4)
    violinStave2.AddNote("A440", 4)
    violinStave2.AddNote("E3", 1)
    violinStave2.AddNote("A2", 1)
    violinStave2.AddNote("E3", 0.5)
    violinStave2.AddNote("A440", 0.5)
    violinStave2.AddNote("E4", 1)
    violinStave2.AddNote("A440", 4)

    musicSheetWave = MusicSheet.GetWave()
    WriteWaveToFile(musicSheetWave, testMusicFile.sampleRate, "PlotWaves\TestMusicDuetWave.txt")

    testMusicFile.ClearAudioData()
    testMusicFile.AddToAudioData(musicSheetWave)
    testMusicFile.WriteFile()
    testMusicFile.PrintFile()
    
