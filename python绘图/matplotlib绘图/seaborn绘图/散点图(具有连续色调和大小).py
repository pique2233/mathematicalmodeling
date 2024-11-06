# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(6, 15))
# 将主题设置为白色风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
planets = sns.load_dataset("planets")

# 创建自定义颜色映射
cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
# 绘制散点图
g = sns.relplot(
    data=planets,
    x="distance", y="orbital_period",
    hue="year", size="mass",
    palette=cmap, sizes=(10, 200),
)
# 设置坐标轴比例为对数
g.set(xscale="log", yscale="log")
# 设置网格线
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
# 去除边框
g.despine(left=True, bottom=True)

plt.show()