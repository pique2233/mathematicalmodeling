# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(8, 8))
# 将主题设置为白色风格
sns.set_theme(style="white")

# 加载示例数据集
df = sns.load_dataset("penguins")
# 绘制一个散点图矩阵
g = sns.PairGrid(df, diag_sharey=False)
# 在散点图矩阵的upper区域(上三角)绘制散点图
g.map_upper(sns.scatterplot, s=15)
# 在散点图矩阵的lower区域(下三角)绘制密度图
g.map_lower(sns.kdeplot)
# 在散点图矩阵的diag区域(对角线)绘制密度图
g.map_diag(sns.kdeplot, lw=2)

plt.show()
