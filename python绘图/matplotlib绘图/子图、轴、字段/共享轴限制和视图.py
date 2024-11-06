# 引入所需库
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


t = np.arange(0, 10, 0.01)

ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))

# sharex=ax1 表示这个区域与 ax1 共享 x 轴坐标轴
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))

plt.show()