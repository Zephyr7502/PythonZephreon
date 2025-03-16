import numpy as np
import matplotlib.pyplot as plt
# 设置采样参数
fs = 500 #采样频率
t = np.linspace(0, 1, fs)
#生成正弦信号
frequency = 5 #信号频率
signal = np.sin(2*np.pi*frequency*t)
#添加噪声
noise = 0.5*np.random.randn(len(t))
noisy_signal=signal+noise

def moving_average(signal1, window_size):
    """
    Apply a moving average filter to the input signal.

    Parameters:
    signal1 (numpy array): The input signal to be filtered.
    window_size (int): The size of the moving window.

    Returns:
    numpy array: The filtered signal.
    """
    filtered_signal = np.convolve(signal1,np.ones(window_size)/window_size, mode= 'same')
    return filtered_signal



window_size= 10
filtered_signal = moving_average(noisy_signal,window_size)




#绘制正弦信号
plt.figure(figsize=(10,4))
plt.plot(t, noisy_signal, label='noisy signal',color='orange', alpha=0.5)
plt.plot(t,filtered_signal,label='filtered signal',linewidth=2)
plt.xlabel('time(second)')
plt.ylabel('amplitude')
plt.title(' comparison before and after filtering')
plt.legend()
plt.show()




