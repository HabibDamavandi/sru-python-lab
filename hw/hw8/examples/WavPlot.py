#ترسیم شکل موج فایل صوتی با پایتون
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open('Windows Logon.wav','r')


signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=np.int16)

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()
