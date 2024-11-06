# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# 设置随机数种子
rng = np.random.default_rng(19680801)
N_points = 100000
# 定义了直方图柱子数量
n_bins = 20

# 生成包含100000个标准正态分布的随机数数组
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5
# sharey=True 表示两个子图的y轴共享同一个坐标轴
# tight_layout=True 表示自动调整子图之间的间距
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
# 绘制直方图
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()