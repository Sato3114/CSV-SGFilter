import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 設定
csvPath = ''                                        # CSVファイルのパス
dt = 0.0001                                         # サンプリング間隔
windowLength = 55                                   # フィルタ窓長さ
polyOrder = 5                                       # 近似式の次数
plotReadData = True                                 # グラフへ元データをプロット
deleteNaN = True                                    # 配列中のNaNを削除するか

# 処理
read = np.genfromtxt(csvPath, delimiter=',', dtype='float')
if deleteNaN:
    data = read[np.isfinite(read)]
else:
    data = read

n = data.size
t = np.linspace(1, n, n) * dt - dt
# print(t)
# print(data)
# print(n)

y = signal.savgol_filter(data, windowLength, polyOrder)

plt.figure(figsize=(12, 9))
if plotReadData:
    plt.plot(t, data, "m")
else:
    pass

plt.plot(t, y)
plt.show()
