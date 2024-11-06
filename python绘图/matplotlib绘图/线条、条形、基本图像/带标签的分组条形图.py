# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


# 创建数据
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
# 用于控制条形的位置
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
# 绘制分组条形图
for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    # 增加multiplier的值，以便在下一个特征绘制时调整条形的位置
    multiplier += 1
# 设置标签&图题
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
# 设置图例
ax.legend(loc='upper left', ncols=3)
# 设置y轴范围
ax.set_ylim(0, 250)

plt.show()