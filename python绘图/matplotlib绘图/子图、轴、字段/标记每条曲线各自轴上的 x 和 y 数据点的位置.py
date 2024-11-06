# 引入所需库
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import EventCollection
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)

# 将xdata数组分成两部分，生成两个随机数组xdata1和xdata2
xdata = np.random.random([2, 10])
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# 对xdata1和xdata2进行排序
xdata1.sort()
xdata2.sort()

# 创建两个数组ydata1和ydata2
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

# 绘制图像
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

# 创建两个事件集合xevents1和xevents2，分别用于表示xdata1和xdata2的标记
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# 创建两个事件集合yevents1和yevents2，分别用于表示ydata1和ydata2的标记
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# 将xevents1和xevents2添加到ax中
# 将yevents1和yevents2添加到ax中
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# 设置x轴和y轴范围
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
# 设置图表标题
ax.set_title('line plot with data points')


plt.show()