# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.ticker import AutoMinorLocator
matplotlib.use('TkAgg')

# 创建图形和坐标轴
fig, ax = plt.subplots(layout='constrained')
# 创建随机数据作为原始数据，将其绘制在坐标轴上，标签为'Plotted data'
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

# 创建随机数据作为原始数据，将其绘制在坐标轴上，标签为'Transform data'
xold = np.arange(0, 11, 0.2)
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)
ax.plot(xold[3:], xnew[3:], label='Transform data')
# 设置x轴的标签为'X [m]'
ax.set_xlabel('X [m]')
# 添加图例
ax.legend()

# 定义两个函数 forward 和 inverse，用于将原始数据和变换后数据进行相互转换
def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)
# 创建一个次要的x轴，并将其放置在顶部
# 设置次要x轴的刻度 locator 为 AutoMinorLocator()
secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
# 设置次要x轴的标签为'$X_{other}$'
secax.set_xlabel('$X_{other}$')
plt.show()