# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

t = np.arange(-1, 2, .01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

# 使用ax.plot()函数在坐标轴上绘制了t和s的关系图
ax.plot(t, s)
# 使用ax.axhline()函数绘制了两条水平线，一条红色，一条黑色。红色水平线跨越整个x轴范围，黑色水平线跨越整个y轴范围
ax.axhline(linewidth=8, color='#d62728')
ax.axhline(y=1)
# 使用ax.axvline()函数绘制了一条垂直线，跨越整个y轴范围
ax.axvline(x=1)
# 使用ax.axvline()函数绘制了一条蓝色垂直线，跨越了y轴上方的半部分
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
# 使用ax.axhline()函数绘制了一条默认的黑色水平线，跨越了y轴的中间一半范围
ax.axhline(y=.5, xmin=0.25, xmax=0.75)
# 使用ax.axline()函数绘制了一条无限长的黑色线，从(0, 0)点延伸到(1, 1)点
ax.axline((0, 0), (1, 1), color='k')
# 使用ax.axhspan()函数绘制了一个灰色矩形，跨越了y轴上0.25到0.75的范围
ax.axhspan(0.25, 0.75, facecolor='0.5')
# 使用ax.axvspan()函数绘制了一个绿色矩形，跨越了x轴上1.25到1.55的范围
ax.axvspan(1.25, 1.55, facecolor='#2ca02c')

plt.show()