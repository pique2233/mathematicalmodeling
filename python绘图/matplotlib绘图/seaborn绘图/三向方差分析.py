# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(6, 15))
# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
exercise = sns.load_dataset("exercise")

# 绘制三向方差分析
g = sns.catplot(
    data=exercise, x="time", y="pulse", hue="kind", col="diet",
    capsize=.2, palette="YlGnBu_d", errorbar="se",
    kind="point", height=6, aspect=.75,
)
# 去除左边框
g.despine(left=True)
plt.show()