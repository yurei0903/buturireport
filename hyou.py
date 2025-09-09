# librosaをインポート
import librosa
# numpyをインポート（配列を生成するため）
import numpy as np
import matplotlib.pyplot as plt

# 音楽ファイルのパスを設定（例："/foldername/filename.mp3"）
file_name = "mi1.wav"
noise_file = "noise.wav"
# loadメソッドでy=音声信号の値（audio time series）、sr=サンプリング周波数（sampling rate）を取得
# file_name = "heikin_majac.wav"
print(file_name)
y, sr = librosa.load(file_name, sr=44100)


# 時間 = yのデータ数 / サンプリング周波数(#サンプリング周波数は1秒間に何回標本化を行うかを示す値)
print("サンプリング周波数:", sr)
print(type(y))
# x = np.zeros(int(sr / 10))
# for i in range(0, int(sr / 10)):
#   x[i] = y[i]

time = np.arange(0, len(y)) / sr

plt.plot(time, y)
plt.xlabel("Time(s)")
plt.ylabel("Sound Amplitude")

# グラフを表示
plt.show()
x_haning = y * np.hamming(len(y))
# plt.plot(time, x_haning)
# plt.xlabel("Time(s)")
# plt.ylabel("Sound Amplitude")
# plt.show()
x_fft = np.fft.fft(y)
x_fre = np.fft.fftfreq(len(x_fft), d=1 / sr)
plt.plot(x_fre[:len(x_fre) // 2], np.abs(x_fft)[:len(x_fre) // 2])
plt.xlabel("Frequency(Hz)")
plt.ylabel("Power spectrum")
plt.xlim(0, 2000)
plt.show()


x_pwr = librosa.feature.rms(y=y)
x_db = librosa.amplitude_to_db(x_pwr, ref=np.max)[0]
time = librosa.times_like(x_db, sr=sr)
# print(x_db)
# print(len(time))
plt.plot(time, x_db)
plt.xlabel("Time(s)")
plt.ylabel("Power spectrum(dB)")
plt.ylim(-100, 0)

plt.show()
