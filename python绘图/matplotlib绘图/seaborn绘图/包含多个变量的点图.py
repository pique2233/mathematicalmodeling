# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(8, 8))
# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
crashes = sns.load_dataset("car_crashes")

# 绘制点图
g = sns.PairGrid(crashes.sort_values("total", ascending=False),
                 x_vars=crashes.columns[:-3], y_vars=["abbrev"],
                 height=10, aspect=.25)

# 设置点大小、线宽、颜色
g.map(sns.stripplot, size=10, orient="h", jitter=False,
      palette="flare_r", linewidth=1, edgecolor="w")

# 将x轴的刻度范围设置为(0,25)，将x轴标签设置为"Crashes"，将y轴标签设置为""
g.set(xlim=(0, 25), xlabel="Crashes", ylabel="")

# 包含每个子图标题的列表
titles = ["Total crashes", "Speeding crashes", "Alcohol crashes",
          "Not distracted crashes", "No previous crashes"]
# 在循环中，它使用ax.set()函数为每个子图设置标题，并将x轴的网格设置为False，将y轴的网格设置为True
for ax, title in zip(g.axes.flat, titles):

    # Set a different title for each axes
    ax.set(title=title)

    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)
# 左侧和底部边框去除
sns.despine(left=True, bottom=True)

plt.show()
