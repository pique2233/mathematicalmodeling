# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)
# 设置直方图的bin数为10
n_bins = 10
x = np.random.randn(1000, 3)
# 创建2x2子图，将子图分别赋给ax0, ax1, ax2, ax3
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

# 颜色列表
colors = ['red', 'tan', 'lime']
# 使用histtype参数设置为'bar'，表示绘制条形图
# 使用density参数设置为True，表示计算每个bin的概率密度，而不是计数
# 使用color参数设置颜色列表
# 使用label参数设置颜色列表，用于添加图例
ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('bars with legend')

# 使用stacked参数设置为True，表示将多个直方图堆叠在一起
ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
ax1.set_title('stacked bar')

# 使用fill参数设置为False，表示不填充直方图的内部
ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
ax2.set_title('stack step (unfilled)')

# 包含三个列表的列表x_multi
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('different sample sizes')

fig.tight_layout()
plt.show()