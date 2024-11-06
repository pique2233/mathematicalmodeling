# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(8, 8))
# 将主题设置为暗色网格风格
sns.set_theme(style="darkgrid")

# 加载示例数据集
iris = sns.load_dataset("iris")

# 设置坐标轴的显示比例，使其具有相同的比例
ax.set_aspect("equal")

# 绘制双变量联合核密度函数图
sns.kdeplot(
    data=iris.query("species != 'versicolor'"),
    x="sepal_width",
    y="sepal_length",
    hue="species",
    thresh=.1,
)
plt.show()