# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(8, 8))
# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
titanic = sns.load_dataset("titanic")

# 绘制配对分类图
g = sns.PairGrid(titanic, y_vars="survived",
                 x_vars=["class", "sex", "who", "alone"],
                 height=5, aspect=.5)

# 将散点图改为点图、调整y轴显示范围、去除边框
g.map(sns.pointplot, color="xkcd:plum")
g.set(ylim=(0, 1))
sns.despine(fig=g.fig, left=True)
plt.show()