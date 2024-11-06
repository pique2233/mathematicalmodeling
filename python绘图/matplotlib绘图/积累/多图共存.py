import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

# 定义辅助函数
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center", fontsize=12, color='gray')
        ax.tick_params(labelbottom=False, labelleft=False)

# 创建figure对象并设置尺寸（宽度x高度，单位：英寸）
fig = plt.figure(figsize=(10, 8), layout="constrained")

# 定义3x3的网格布局，并设置子图之间的间距
gs = GridSpec(3, 3, figure=fig, wspace=0.2, hspace=0.2)

# 在指定网格位置创建子图
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

# 添加图表示例
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), label='sin(x)')
ax1.legend()

ax2.scatter(x, np.random.randn(100), color='r')
ax3.bar([1, 2, 3], [3, 2, 5])

ax4.hist(np.random.randn(100), bins=15, color='g')
ax5.pie([15, 30, 45, 10], labels=['A', 'B', 'C', 'D'])

# 设置图形标题并格式化子图
fig.suptitle("GridSpec with Plots")
format_axes(fig)

# 显示图形
plt.show()



"""
1.	ax1 = fig.add_subplot(gs[0, :])
	•	位置： 位于第1行，跨越所有列（从第1列到最后一列）。
	•	作用： 创建一个横跨整个第一行的子图 ax1。
	2.	ax2 = fig.add_subplot(gs[1, :-1])
	•	位置： 位于第2行，跨越从第1列到倒数第二列（即不包括最后一列）。
	•	作用： 创建一个占据第2行的大部分区域（除了最后一列）的子图 ax2。
	3.	ax3 = fig.add_subplot(gs[1:, -1])
	•	位置： 从第2行到第3行的最后一列（垂直方向上跨越两行）。
	•	作用： 创建一个占据第2和第3行最后一列的子图 ax3，这个子图垂直方向上跨越了两行。
	4.	ax4 = fig.add_subplot(gs[-1, 0])
	•	位置： 位于最后一行（第3行）的第一列。
	•	作用： 创建一个在最后一行第1列位置的子图 ax4。
	5.	ax5 = fig.add_subplot(gs[-1, -2])
	•	位置： 位于最后一行（第3行）的倒数第二列。
	•	作用： 创建一个在最后一行倒数第二列位置的子图 ax5。
	
	
	0       1       2
         +-------+-------+-------+
         | (0,0) | (0,1) | (0,2) |
列索引:  +-------+-------+-------+
         | (1,0) | (1,1) | (1,2) |
         +-------+-------+-------+
         | (2,0) | (2,1) | (2,2) |
         +-------+-------+-------+
"""



"""
# 引入所需库
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(layout="constrained")

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

fig.suptitle("GridSpec")
format_axes(fig)

plt.show()

"""
