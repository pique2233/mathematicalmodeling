# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

fig, ax = plt.subplots()

# 创建散点图
sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
# 设置y轴和x轴的标签。loc参数用于指定标签的位置，top表示标签在y轴上方
ax.set_ylabel('YLabel', loc='top')
ax.set_xlabel('XLabel', loc='left')

# 添加颜色条
cbar = fig.colorbar(sc)
# 设置颜色条的标签。loc参数用于指定标签的位置，top表示标签在颜色条上方
cbar.set_label("ZLabel", loc='top')

plt.show()