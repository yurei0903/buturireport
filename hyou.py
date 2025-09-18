import librosa
import numpy as np
import matplotlib.pyplot as plt


file_name = "rokuonsitaoto\do2.wav"
# loadメソッドでy=音声信号の値（audio time series）、sr=サンプリング周波数（sampling rate）を取得
print(file_name)
y, sr = librosa.load(file_name, sr=44100)


# 時間 = yのデータ数 / サンプリング周波数(#サンプリング周波数は1秒間に何回標本化を行うかを示す値)
print("サンプリング周波数:", sr)
print(type(y))


time = np.arange(0, len(y)) / sr

plt.plot(time, y)
plt.ylim(-0.35, 0.35)
plt.xlabel("time(s)")
plt.ylabel("Sound Amplitude")

# グラフを表示
plt.show()
x_hamming = y * np.hamming(len(y))
x_fft = np.fft.fft(x_hamming)
x_fre = np.fft.fftfreq(len(x_fft), d=1 / sr)
plt.plot(x_fre[:len(x_fre) // 2], np.abs(x_fft)[:len(x_fre) // 2])
plt.xlabel("Frequency(Hz)")
plt.ylabel("Power spectrum")
plt.xlim(0, 2000)
plt.show()
