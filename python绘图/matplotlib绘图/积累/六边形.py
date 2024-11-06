import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
#大规模数据集的可视化，代替散点图
# 设置随机数种子
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()

# 创建图形和子图
fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=True, figsize=(10, 5))
plt.subplots_adjust(wspace=0.3)  # 调整子图之间的间距

# 绘制第一个六边形分箱图
hb = ax0.hexbin(x, y, gridsize=50, cmap='inferno')
ax0.set(xlim=xlim, ylim=ylim)
ax0.set_title("Hexagon binning", fontsize=14, fontweight='bold')
cb = fig.colorbar(hb, ax=ax0, label='Counts')
cb.ax.tick_params(labelsize=10)  # 调整颜色条刻度的字体大小

# 绘制第二个六边形分箱图（对数刻度）
hb = ax1.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax1.set(xlim=xlim, ylim=ylim)
ax1.set_title("Log-scaled color", fontsize=14, fontweight='bold')
cb = fig.colorbar(hb, ax=ax1, label='Log Counts')
cb.ax.tick_params(labelsize=10)  # 调整颜色条刻度的字体大小

# 设置主标题
fig.suptitle("Hexbin Plot with Different Color Scales", fontsize=16, fontweight='bold')

plt.show()