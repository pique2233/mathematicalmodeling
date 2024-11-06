# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

#  设置图大小
f, ax = plt.subplots(figsize=(9, 6))
# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

#  加载示例数据集
df = sns.load_dataset("anscombe")

#  绘制散点图,并显示每个数据集中的线性回归结果
sns.lmplot(
    data=df, x="x", y="y", col="dataset", hue="dataset",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)
plt.show()
