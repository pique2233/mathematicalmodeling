# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))
# 将主题设置为带有白色网格的风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
iris = sns.load_dataset("iris")

# "Melt" the dataset to "long-form" or "tidy" representation
# 将这个数据框转换为一个新数据框，其中每个观测值都有一个唯一的measurement变量
iris = iris.melt(id_vars="species", var_name="measurement")

# 去除matplotlib绘图中的边框
sns.despine(bottom=True, left=True)

# 绘制散点图
sns.stripplot(
    data=iris, x="value", y="measurement", hue="species",
    dodge=True, alpha=.25, zorder=1, legend=False,
)

# 绘制点线图、在分组之间使用菱形标记
sns.pointplot(
    data=iris, x="value", y="measurement", hue="species",
    dodge=.8 - .8 / 3, palette="dark", errorbar=None,
    markers="d", markersize=4, linestyle="none",
)

# 将图例放在右下角、图例分为3列、显示图例的边框
sns.move_legend(
    ax, loc="lower right", ncol=3, frameon=True, columnspacing=1, handletextpad=0,
)
plt.show()