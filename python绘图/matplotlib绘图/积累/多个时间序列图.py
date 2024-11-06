import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建自定义数据集
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data = {
    "month": np.tile(months, 10),  # 10年，每年12个月
    "year": np.repeat(np.arange(2010, 2020), 12),
    "passengers": np.random.randint(100, 1000, size=120) + np.linspace(0, 200, 120)
}
df = pd.DataFrame(data)

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))
# 设置为暗色主题
sns.set_theme(style="dark")

# 创建一个线图，其中每个变量都具有自己的行和列
g = sns.relplot(
    data=df,
    x="month", y="passengers", col="year", hue="year",
    kind="line", palette="crest", linewidth=4, zorder=5,
    col_wrap=3, height=2, aspect=1.5, legend=False,
)

# 遍历每个子图、添加标题注释
for year, ax in g.axes_dict.items():
    ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")
    sns.lineplot(
        data=df, x="month", y="passengers", units="year",
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