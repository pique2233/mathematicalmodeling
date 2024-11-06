# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)

# 创建了一个包含30个随机数的列表，这些随机数的范围在0到0.2之间。
# pts[[3, 14]] += .8 将第3个和第14个随机数增加0.8，使得它们的范围在0.8到1之间
pts = np.random.rand(30)*.2
pts[[3, 14]] += .8

# 创建了一个包含两个子图的图形，并将其共享x轴;调整子图之间的空间为0.05
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.05)

ax1.plot(pts)
ax2.plot(pts)
ax1.set_ylim(.78, 1.)
ax2.set_ylim(0, .22)

# 隐藏了两个子图的x轴底部和顶部边框
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
# 将x轴的刻度线移动到顶部子图和底部子图的顶部
ax1.xaxis.tick_top()
ax2.xaxis.tick_bottom()
# 隐藏了两个子图的x轴底部和顶部边框的刻度线
ax1.tick_params(labeltop=False)

# 表示镜像线的长度
d = .5
# 创建了一个字典，用于存储镜像线的属性，如标记类型、大小、颜色等
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
# 在顶部子图和底部子图的x轴上绘制了镜像线
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

plt.show()