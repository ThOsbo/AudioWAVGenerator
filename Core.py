import ByteFiles

if __name__ == "__main__" :
    testFileRead = ByteFiles.wavFile("TestAudio\sound.wav")
    testFileRead.PrintFile()
    print("\n")

    testFileWrite = ByteFiles.wavFile("TestAudio\TestFile.wav")
    testFileWrite.WriteFile()
    testFileWrite.PrintFile()
    print("\n")