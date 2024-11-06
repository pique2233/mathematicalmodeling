# 引入所需库
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)

ax1 = plt.subplot(311)
plt.plot(t, s1)
plt.tick_params('x', labelsize=6)
# 表示这个区域与 ax1 共享 x 轴坐标轴
ax2 = plt.subplot(312, sharex=ax1)
plt.plot(t, s2)
plt.tick_params('x', labelbottom=False)
# sharex 和 sharey 参数分别用于指定子图是否共享x轴和y轴
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
plt.plot(t, s3)
plt.xlim(0.01, 5.0)
plt.show()