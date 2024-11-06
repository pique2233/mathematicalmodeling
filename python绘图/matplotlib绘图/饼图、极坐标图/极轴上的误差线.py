# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
# 在极坐标图中绘制误差线
# theta和r分别表示数据点的角度和距离
# xerr和yerr分别表示角度和距离的误差
# capsize表示误差线的长度
# fmt表示数据点的形状，c表示数据点的颜色
ax.errorbar(theta, r, xerr=0.25, yerr=0.1,
            capsize=7, fmt="o", c="seagreen")

ax.set_title("Pretty polar error bars")
plt.show()