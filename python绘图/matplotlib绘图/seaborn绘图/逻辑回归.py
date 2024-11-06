# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(6, 6))
# 将主题设置为暗色网格风格
sns.set_theme(style="darkgrid")

# 加载示例数据集
df = sns.load_dataset("titanic")

# 定义了一个颜色映射
pal = dict(male="#6495ED", female="#F08080")
# 绘制了一个线性回归模型
g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
               palette=pal, y_jitter=.02, logistic=True, truncate=False)
# 设置 x 轴和 y 轴的范围
g.set(xlim=(0, 80), ylim=(-.05, 1.05))

plt.show()