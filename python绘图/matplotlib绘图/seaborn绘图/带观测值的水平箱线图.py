# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))
# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

# 将x轴的刻度设置为对数刻度
ax.set_xscale("log")

# 加载示例数据集
planets = sns.load_dataset("planets")

# 绘制水平箱线图
sns.boxplot(
    planets, x="distance", y="method", hue="method",
    whis=[0, 100], width=.6, palette="vlag"
)

# 在水平箱线图中绘制散点图
sns.stripplot(planets, x="distance", y="method", size=4, color=".3")

# 在x轴上添加网格线
ax.xaxis.grid(True)
# 移除y轴标签
ax.set(ylabel="")
# 移除图像周围的非关键线
sns.despine(trim=True, left=True)
plt.show()