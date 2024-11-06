# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)
# 制作数据
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
# labels: 四个标签的列表 A、B、C、D
labels = list('ABCD')
# fs: 字体大小 10
fs = 10  # fontsize

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
# 绘制箱线图
axs[0, 0].boxplot(data, tick_labels=labels)
# 设置图表的标题和标题字体大小
axs[0, 0].set_title('Default', fontsize=fs)

# showmeans 表示显示箱线图中的均值
axs[0, 1].boxplot(data, tick_labels=labels, showmeans=True)
axs[0, 1].set_title('showmeans=True', fontsize=fs)
# meanline 表示是否在箱线图上显示均值线
axs[0, 2].boxplot(data, tick_labels=labels, showmeans=True, meanline=True)
axs[0, 2].set_title('showmeans=True,\nmeanline=True', fontsize=fs)
# showbox设置为False表示不显示箱线图的箱体
# showcaps设置为False表示不显示箱线图的顶端和底端线
axs[1, 0].boxplot(data, tick_labels=labels, showbox=False, showcaps=False)
# 格式化标题
tufte_title = 'Tufte Style \n(showbox=False,\nshowcaps=False)'
axs[1, 0].set_title(tufte_title, fontsize=fs)
# notch参数设置为True表示使用斜线填充箱线图
# bootstrap参数设置为10000表示使用bootstrap方法进行异常值检测
axs[1, 1].boxplot(data, tick_labels=labels, notch=True, bootstrap=10000)
axs[1, 1].set_title('notch=True,\nbootstrap=10000', fontsize=fs)
# showfliers设置为False表示不显示异常值
axs[1, 2].boxplot(data, tick_labels=labels, showfliers=False)
axs[1, 2].set_title('showfliers=False', fontsize=fs)

# 以此对子图进行操作
for ax in axs.flat:
    # 纵坐标以对数形式显示
    ax.set_yscale('log')
    # 不显示纵坐标轴上的刻度标签
    ax.set_yticklabels([])

# 调整子图之间的间距
# hspace=0.4 表示子图之间的垂直间距为 0.4 英寸
fig.subplots_adjust(hspace=0.4)
plt.show()