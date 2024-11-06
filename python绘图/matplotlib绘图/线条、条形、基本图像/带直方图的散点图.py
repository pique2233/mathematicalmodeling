# 引入所需库

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib
matplotlib.use('TkAgg')


# 设置随机种子
np.random.seed(19680801)

# 创建散点图数据
x = np.random.randn(1000)
y = np.random.randn(1000)

# 绘制散点图以及其对应的直方图函数
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')



fig = plt.figure(figsize=(6, 6))
# 创建图形对象
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# 将子图分配给三个不同的坐标轴
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# 绘制散点图和直方图
scatter_hist(x, y, ax, ax_histx, ax_histy)

plt.show()