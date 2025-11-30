import matplotlib.pyplot as plt
import numpy as np
import wave
import simpleaudio as sa

###############################################################################
# Parameters
#
amplitude = 2
offset = amplitude/2
freq = 100
sample_rate = 44100
num_samples = 2**14
start_time = 0
end_time = num_samples / sample_rate
inc = amplitude*(freq/sample_rate)

###############################################################################
# Waveform synthesis
time = np.arange(start_time, end_time, 1/sample_rate) # Time vector
sawtooth = np.zeros(len(time))
triangle = np.zeros(len(time))
for s in range(num_samples-1):
    if sawtooth[s] >= (amplitude):
        sawtooth[s] = 0
    sawtooth[s+1] = sawtooth[s] + inc
sawtooth = sawtooth - offset

for s in range(num_samples-1):
    if abs(triangle[s]) >= (amplitude/2):
        inc = -inc
    triangle[s+1] = triangle[s] + 2*inc
#triangle = triangle - offset
###############################################################################
# Frequency analisys
sawtooth_fft = np.fft.fft(sawtooth)
triangle_fft = np.fft.fft(triangle)
freq_vector = np.arange(0, sample_rate, sample_rate / (num_samples))

###############################################################################
# Waveform conditioning
audio_processed = sawtooth * (2**15 - 1)
audio_processed = audio_processed.astype(np.int16) # Convert to 16-bit data
###############################################################################
# Audio playback
#play_obj = sa.play_buffer(signal_raw, 1, 2, 44100) # Start playback
#play_obj.wait_done() # Wait for playback to finish before exiting
play_obj = sa.play_buffer(audio_processed, 1, 2, sample_rate) # Start playback
play_obj.wait_done() # Wait for playback to finish before exiting
###############################################################################
# Plot audio signals
fig1, ax1 = plt.subplots(2,2)
ax1[0, 0].plot(time,sawtooth)
ax1[0, 0].grid()
ax1[0, 0].set_title('Sawtooth')
ax1[0, 1].semilogx(freq_vector, 20*np.log10(np.abs(sawtooth_fft)))
ax1[0, 1].set_xlim(left=20, right=10000)
ax1[0 ,1].set_ylim(bottom=20, top=80)
ax1[0, 1].grid()
ax1[0, 1].set_title('Sawtooth')
ax1[1, 0].plot(time,triangle)
#ax1[0, 1].set_ylim(bottom=-1, top=1)
ax1[1, 0].grid()
ax1[1, 0].set_title('Triangle')
ax1[1, 1].semilogx(freq_vector, 20*np.log10(np.abs(triangle_fft)))
ax1[1, 1].set_xlim(left=20, right=10000)
ax1[1 ,1].set_ylim(bottom=20, top=80)
ax1[1, 1].grid()
ax1[1, 1].set_title('Triangle')
plt.show()
