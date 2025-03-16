import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt

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
    filtered_signal = np.convolve(signal1, np.ones(window_size) / window_size, mode='same')
    return filtered_signal

def exponential_moving_average(signal1, alpha):
    ema = np.zeros_like(signal1)
    ema[0] = signal1[0]
    for i in range(1, len(signal1)):
        ema[i] = alpha * signal1[i] + (1 - alpha) * ema[i - 1]
    return ema

def gaussian_filter(signal1, sigma):
    return gaussian_filter1d(signal1, sigma)

def median_filter(signal1, kernel_size):
    return medfilt(signal1, kernel_size)

# 应用不同的滤波器
window_size = 10
alpha = 0.1
sigma = 2
kernel_size = 5

filtered_signal_ma = moving_average(noisy_signal, window_size)
filtered_signal_ema = exponential_moving_average(noisy_signal, alpha)
filtered_signal_gaussian = gaussian_filter(noisy_signal, sigma)
filtered_signal_median = median_filter(noisy_signal, kernel_size)

# 绘制信号
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.plot(t, noisy_signal, label='noisy signal', color='orange', alpha=0.5)
plt.plot(t, filtered_signal_ma, label='moving average', linewidth=2)
plt.xlabel('time(second)')
plt.ylabel('amplitude')
plt.title('Moving Average Filter')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(t, noisy_signal, label='noisy signal', color='orange', alpha=0.5)
plt.plot(t, filtered_signal_ema, label='exponential moving average', linewidth=2)
plt.xlabel('time(second)')
plt.ylabel('amplitude')
plt.title('Exponential Moving Average Filter')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(t, noisy_signal, label='noisy signal', color='orange', alpha=0.5)
plt.plot(t, filtered_signal_gaussian, label='gaussian filter', linewidth=2)
plt.xlabel('time(second)')
plt.ylabel('amplitude')
plt.title('Gaussian Filter')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(t, noisy_signal, label='noisy signal', color='orange', alpha=0.5)
plt.plot(t, filtered_signal_median, label='median filter', linewidth=2)
plt.xlabel('time(second)')
plt.ylabel('amplitude')
plt.title('Median Filter')
plt.legend()

plt.tight_layout()
plt.show()