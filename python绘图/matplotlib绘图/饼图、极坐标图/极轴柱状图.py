# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)

# 定义了三个变量N、theta和radii，分别表示柱状图的数量、角度和半径
# N被赋为20，表示要创建20个柱状图
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
# 根据半径值生成颜色值
colors = plt.cm.viridis(radii / 10.)

# 创建极坐标系
ax = plt.subplot(projection='polar')
# 在极坐标系中创建柱状图
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)

plt.show()

