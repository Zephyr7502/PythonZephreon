import numpy as np
import matplotlib.pyplot as plt
# 设置采样参数
fs = 500 #采样频率
t = np.linspace(0, 1, fs)
#生成正弦信号
frequency = 5 #信号频率
signal = np.sin(2*np.pi*frequency*t)
#绘制正弦信号
plt.figure(figsize=(10,4))
plt.plot(t, signal, label='original sine signal')
plt.xlabel('time(second)')
plt.ylabel('amplitude')
plt.title('sine signal')
plt.legend()
plt.show()




