# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))

# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

# 加载示例数据集
planets = sns.load_dataset("planets")
# 创建一个联合图对象
g = sns.JointGrid(data=planets, x="year", y="distance", marginal_ticks=True)
# 设置对数刻度
g.ax_joint.set(yscale="log")

# 创建了一个坐标轴对象
cax = g.figure.add_axes([.15, .55, .02, .2])

# 绘制联合直方图和边缘直方图
g.plot_joint(
    sns.histplot, discrete=(True, False),
    cmap="light:#03012d", pmax=.8, cbar=True, cbar_ax=cax
)
# 设置图例
g.plot_marginals(sns.histplot, element="step", color="#03012d")
plt.show()