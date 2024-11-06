# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib
matplotlib.use('TkAgg')

# 创建数据
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

# 格式化浮点数函数
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"


fig, ax = plt.subplots()
# 绘制等高线
CS = ax.contour(X, Y, Z)
# 添加标签
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
plt.show()