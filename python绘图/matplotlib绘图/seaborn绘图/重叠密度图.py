# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))

# 将主题设置为白色风格、将轴的颜色设置为黑色
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# 创建一个随机数列
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x=x, g=g))
m = df.g.map(ord)
df["x"] += m

# 使用cubehelix颜色映射为每个类别创建了一个颜色序列
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
# 创建一个FacetGrid对象，该对象用于绘制不同类别之间的密度分布图
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=.5, palette=pal)

# 使用kdeplot函数绘制密度分布图，并使用refline函数添加了一条参考线
g.map(sns.kdeplot, "x",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)
g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)


# 在图形的坐标轴上添加标签
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)
g.map(label, "x")

# 调整图形布局，将每个子图之间的垂直间距减小到最小
g.figure.subplots_adjust(hspace=-.25)

# 移除网格标题
g.set_titles("")
# 移除y轴标签
g.set(yticks=[], ylabel="")
# 删除网格下边框和左边框
g.despine(bottom=True, left=True)

plt.show()