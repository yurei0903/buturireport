import librosa
import numpy as np
import wave
import time
file = []
frame = 44100       # サンプルレート（Hz）
jikan = 3     # 録音時間（秒）
channels = 1
# loadメソッドでy=音声信号の値（audio time series）、sr=サンプリング周波数（sampling rate）を取得
for i in range(1, 11):
  file_name = "majac" + str(i) + ".wav"
  print(file_name)
  data, sr = librosa.load(file_name, sr=frame)
  file.append(data)
  print("サンプリング周波数:", sr)
print(len(file[0]))
heikin = np.zeros(len(file[0]), dtype=np.float32)
for i in range(0, len(file[0])):
  sum = 0
  for j in range(0, 10):
    sum = sum + file[j][i]
  heikin[i] = sum / 10

print(len(heikin))
heikin_int16 = (heikin * 32767).astype(np.int16)

output_file = "heikin_majac.wav"
with wave.open(output_file, 'wb') as wf:
  wf.setnchannels(channels)
  wf.setsampwidth(2)  # 16ビットオーディオの場合、サンプル幅は2バイト
  wf.setframerate(frame)
  wf.writeframes(heikin.tobytes())
