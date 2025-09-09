import librosa
import numpy as np
import soundfile as sf  # soundfileライブラリをsfとしてインポート

file = []
frame = 44100      # サンプルレート（Hz）
num_files = 10     # ファイルの数

# 1. 全てのWAVファイルを読み込む
for i in range(1, num_files + 1):
  file_name = f"majac{i}.wav"  # f-stringを使うとシンプルに書けます
  print(f"読み込み中: {file_name}")
  try:
    # librosa.loadはデフォルトでfloat32のnumpy配列を返す
    data, sr = librosa.load(file_name, sr=frame, mono=True)
    file.append(data)
  except Exception as e:
    print(f"エラー: {file_name} が読み込めませんでした。 {e}")
    continue  # エラーが発生したファイルはスキップ

if not file:
  print("音声ファイルが一つも読み込めませんでした。")
else:
  # 2. 配列の長さを最も短いファイルに合わせる（念のため）
  min_len = min(len(f) for f in file)

  # 同じ長さに切りそろえる
  file_aligned = [f[:min_len] for f in file]

  # 3. 音声データの平均を計算
  # NumPyの機能を使えば、forループなしで高速に平均を計算できる
  heikin = np.mean(np.array(file_aligned), axis=0)

  print("平均化処理が完了しました。")

  # 4. soundfileを使ってファイルに書き出す
  output_file = "heikin_majac.wav"
  # heikin（float配列）とサンプリング周波数を渡すだけでOK
  sf.write(output_file, heikin, frame)

  print(f"正常に {output_file} として保存しました。")
  print(f"再生時間: {len(heikin) / frame:.2f}秒")
