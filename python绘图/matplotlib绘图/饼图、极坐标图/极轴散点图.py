# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)


# 定义三个变量N、r和theta，分别表示散点的数量、极径和极角
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
# 定义变量area，表示每个散点的面积
area = 200 * r**2
# 每个散点的颜色
colors = theta

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
# 绘制散点图
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

plt.show()