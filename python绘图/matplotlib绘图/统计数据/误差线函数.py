# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

fig, ax = plt.subplots()

# 绘制带有误差线的散点图
# xerr和yerr分别表示横纵坐标的误差值
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()