# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)


r = np.arange(0, 2, 0.01)
# 极角theta
theta = 2 * np.pi * r
# 创建极坐标图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# 绘制曲线
ax.plot(theta, r)

# 设置极坐标图的坐标轴范围
ax.set_rmax(2)
# 设置极坐标图的坐标轴刻度
ax.set_rticks([0.5, 1, 1.5, 2])
# 设置极坐标图的坐标轴标签位置
ax.set_rlabel_position(-22.5)
# 设置极坐标图的网格线
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()