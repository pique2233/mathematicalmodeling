# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)

# 生成数据
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2
c = np.sqrt(area)
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
# 绘制散点图
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
# 屏蔽圆
theta = np.arange(0, np.pi / 2, 0.01)
# 绘制屏蔽圆
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()