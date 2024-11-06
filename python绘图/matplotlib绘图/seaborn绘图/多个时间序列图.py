# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))
# 设置为暗色主题
sns.set_theme(style="dark")

# 加载示例数据集
flights = sns.load_dataset("flights")

#  创建一个线图，其中每个变量都具有自己的行和列
g = sns.relplot(
    data=flights,
    x="month", y="passengers", col="year", hue="year",
    kind="line", palette="crest", linewidth=4, zorder=5,
    col_wrap=3, height=2, aspect=1.5, legend=False,
)

# 遍历每个子图、添加标题注释
for year, ax in g.axes_dict.items():

    # Add the title as an annotation within the plot
    ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")

    # Plot every year's time series in the background
    sns.lineplot(
        data=flights, x="month", y="passengers", units="year",
        estimator=None, color=".7", linewidth=1, ax=ax,
    )

# 设置子图的x轴刻度频率
ax.set_xticks(ax.get_xticks()[::2])

# 设置图形标题
g.set_titles("")
# 设置x轴和y轴标签
g.set_axis_labels("", "Passengers")
# 调整子图之间的间距
g.tight_layout()

plt.show()