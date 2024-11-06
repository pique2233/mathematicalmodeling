# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)
# 创建一个包含三个数组的列表 fruit_weights
fruit_weights = [
    np.random.normal(130, 10, size=100),
    np.random.normal(125, 20, size=100),
    np.random.normal(120, 30, size=100),
]
# 创建包含三个字符串的列表labels和包含三个颜色的列表colors
labels = ['peaches', 'oranges', 'tomatoes']
colors = ['peachpuff', 'orange', 'tomato']

#创建一个图形和坐标轴对象fig和ax
fig, ax = plt.subplots()
# 设置坐标轴的y轴标签
ax.set_ylabel('fruit weight (g)')
# patch_artist=True 参数表示填充箱线图的内部颜色
bplot = ax.boxplot(fruit_weights,
                   patch_artist=True,
                   tick_labels=labels)
# 使用zip()函数将bplot['boxes']和colors两个列表中的元素一一对应起来
for patch, color in zip(bplot['boxes'], colors):
    # 设置每个箱线图的填充颜色
    patch.set_facecolor(color)

plt.show()