# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)

# 生成随机数和指数衰减信号
dt = 0.01
t = np.arange(0, 10, dt)
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
# 生成包含噪声信号和正弦波的模拟信号
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]
s = 0.1 * np.sin(2 * np.pi * t) + cnse

fig, (ax0, ax1) = plt.subplots(2, 1, layout='constrained')
# 绘制原始信号
ax0.plot(t, s)
ax0.set_xlabel('Time (s)')
ax0.set_ylabel('Signal')
# 绘制功率谱密度
ax1.psd(s, 512, 1 / dt)

plt.show()