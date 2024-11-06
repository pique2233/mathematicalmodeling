# 引入所需库 双直方图绘制
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# 设置随机数种子
rng = np.random.default_rng(19680801)

# 数据集中的点数和直方图的宽度
N_points = 10_000
bin_width = 0.25
# 生成了两个具有不同均值和标准差的正态分布数据集
dataset1 = np.random.normal(0, 1, size=N_points)
dataset2 = np.random.normal(1, 2, size=N_points)

# 直方图边界
bins = np.arange(np.min([dataset1, dataset2]),
                    np.max([dataset1, dataset2]) + bin_width, bin_width)

fig, ax = plt.subplots()
# 绘制直方图，使用bins作为边界，设置标签为 "Dataset 1"
ax.hist(dataset1, bins=bins, label="Dataset 1",edgecolor="grey",histtype='bar')
# 设置权重weights为-np.ones_like(dataset2)，即直方图的面积变成负值
ax.hist(dataset2, weights=-np.ones_like(dataset2), bins=bins, label="Dataset 2",edgecolor="grey")
# 绘制一条水平线，表示直方图的底部
ax.axhline(0, color="k")
ax.legend()

plt.show()