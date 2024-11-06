# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)

# 均值mu为200，标准差sigma为25
mu = 200
sigma = 25
# 直方图中划分的区间数量
n_bins = 25
# 生成100个服从正态分布的随机数
data = np.random.normal(mu, sigma, size=100)

fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)

# 绘制CDF
axs[0].ecdf(data, label="CDF")
# 绘制累积直方图
n, bins, patches = axs[0].hist(data, n_bins, density=True, histtype="step",
                               cumulative=True, label="Cumulative histogram")
# 计算理论CDF
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
# 绘制理论CDF
axs[0].plot(x, y, "k--", linewidth=1.5, label="Theory")

# 绘制CCDF
axs[1].ecdf(data, complementary=True, label="CCDF")
# 绘制反向累积直方图
axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
            label="Reversed cumulative histogram")
# 绘制理论CCDF
axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="Theory")

# 设置了图表的标题、坐标轴标签和图例，使坐标轴标签在外部显示
fig.suptitle("Cumulative distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()