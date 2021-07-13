# def GenerateSquareWave(duration) :
#     global data, byteRate, bitsPerSample
#     amplitude = 32767
#     frequency = 44100
#     offset = 0

#     numBytes = int(duration * byteRate)
#     swapSign = int(byteRate / frequency)
#     sign = 1

#     for i in range(numBytes) :
#         if (i % swapSign == 0) :
#             sign = sign * -1
#         val = (sign * amplitude) + offset
#         if bitsPerSample == 8 :
#             byte = bytes([val])
#         elif bitsPerSample == 16 :
#             byte = struct.pack("<h", val)
#         data.append(byte)