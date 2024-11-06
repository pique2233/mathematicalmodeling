# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
# 生成两个随机数列nse1和nse2，作为噪声
nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))

# 定义两个正弦波s1和s2
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

# 创建一个2x1的子图，并设置布局为 constrained
fig, axs = plt.subplots(2, 1, layout='constrained')

# 在第一个子图中绘制s1和s2
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

# 在第二个子图中绘制s1和s2的相干性
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')

plt.show()