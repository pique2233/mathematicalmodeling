# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)

# 定义了两个均值mu和标准差sigma
mu_x = 200
sigma_x = 25
mu_w = 200
sigma_w = 10
# 两个大小为100的随机数数组x和w
x = np.random.normal(mu_x, sigma_x, size=100)
w = np.random.normal(mu_w, sigma_w, size=100)


fig, axs = plt.subplots(nrows=2, ncols=2)
# 绘制stepfilled类型的直方图，即在两个连续的条形图之间填充颜色
axs[0, 0].hist(x, 20, density=True, histtype='stepfilled', facecolor='g',
               alpha=0.75)
# 设置标题
axs[0, 0].set_title('stepfilled')
# 绘制step类型的直方图，即只绘制直方图的边框，不填充颜色
axs[0, 1].hist(x, 20, density=True, histtype='step', facecolor='g',
               alpha=0.75)
axs[0, 1].set_title('step')
# 绘制barstacked类型的直方图，即在两个连续的条形图之间填充颜色
axs[1, 0].hist(x, density=True, histtype='barstacked', rwidth=0.8)
axs[1, 0].hist(w, density=True, histtype='barstacked', rwidth=0.8)
axs[1, 0].set_title('barstacked')
# bins参数指定了直方图的边界，使得直方图的宽度不相等
# 绘制bar类型的直方图，即在两个连续的条形图之间填充颜色
bins = [100, 150, 180, 195, 205, 220, 250, 300]
axs[1, 1].hist(x, bins, density=True, histtype='bar', rwidth=0.8)
axs[1, 1].set_title('bar, unequal bins')

# 调整子图之间的间距
fig.tight_layout()
plt.show()