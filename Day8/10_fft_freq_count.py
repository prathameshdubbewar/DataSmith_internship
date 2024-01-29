# REVISE AGAIN

import numpy as np
import matplotlib.pyplot as plt

fs = 1000  
T = 1     
N = fs * T 
t = np.linspace(0, T, N, endpoint=False)

frequencies = [10, 50, 100]  
amplitudes = [1, 0.5, 0.2]    

signal = np.zeros_like(t)
for freq, amp in zip(frequencies, amplitudes):
    signal += amp * np.sin(2 * np.pi * freq * t)

fft_output = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, 1/fs)  

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, color='blue')
plt.title('Synthetic Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(fft_output), color='red')
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(0, fs/2)  
plt.tight_layout()
plt.show()
