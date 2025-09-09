import sounddevice as sd
import numpy as np
import wave
import time
# 録音パラメータ
frame = 44100       # サンプルレート（Hz）
jikan = 3     # 録音時間（秒）
channels = 1     # モノラル（ステレオの場合は2）


def main():
  print("録音まで3秒")
  time.sleep(1)
  print("録音まで2秒")
  time.sleep(1)
  print("録音まで1秒")
  time.sleep(1)
  print("録音開始")
  oto_data = sd.rec(frames=int(jikan * frame), samplerate=frame,
                    channels=channels, dtype='int16')
  sd.wait()
  print(len(oto_data))

  output_file = "aaa.wav"
  with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(2)  # 16ビットオーディオの場合、サンプル幅は2バイト
    wf.setframerate(frame)
    wf.writeframes(oto_data.tobytes())

if __name__ == "__main__":
  main()
