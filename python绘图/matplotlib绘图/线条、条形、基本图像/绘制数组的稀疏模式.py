# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# # 设置随机数种子
np.random.seed(19680801)
# 创建2x2图形
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]

# 生成20x20的随机数组
x = np.random.randn(20, 20)
# 随机将数组中的某些元素设置为0
x[5, :] = 0.
x[:, 12] = 0.

# 在四个子图中绘制随机数组中的非零元素
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)

plt.show()