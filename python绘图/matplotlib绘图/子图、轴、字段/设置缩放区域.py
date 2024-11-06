# 引入所需库
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook
matplotlib.use('TkAgg')


fig, ax = plt.subplots()

# 加载数据
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
# 创建一个名为Z2的二维数组
# 将 Z 复制到 Z2 的指定区域
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z
# extent参数用于设置图像的显示范围
extent = (-3, 4, -4, 3)
# 显示 Z2 图像
ax.imshow(Z2, extent=extent, origin="lower")

# 定义一个放大区域的坐标x1, x2, y1, y2
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
# 创建一个新的坐标轴axins
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    # 将axins的显示范围设置为x1, x2, y1, y2，并将axins的坐标轴刻度标签设置为空
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
# 显示缩放后图像
axins.imshow(Z2, extent=extent, origin="lower")
# 在主坐标轴上显示放大区域的边界
ax.indicate_inset_zoom(axins, edgecolor="black")

plt.show()