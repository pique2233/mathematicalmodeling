# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(8, 8))
# 将主题设置为网格风格
sns.set_theme(style="ticks")

# 加载示例数据集
mpg = sns.load_dataset("mpg")

# 创建一个颜色映射cmap
colors = (250, 70, 50), (350, 70, 50)
cmap = sns.blend_palette(colors, input="husl", as_cmap=True)
# 绘制多分布经验累积概率分布函数图(ECDF)
sns.displot(
    mpg,
    x="displacement", col="origin", hue="model_year",
    kind="ecdf", aspect=.75, linewidth=2, palette=cmap,
)
plt.show()