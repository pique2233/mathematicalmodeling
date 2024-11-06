# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(6.5, 6.5))

# 加载示例数据集
diamonds = sns.load_dataset("diamonds")

# 移除图像的左部和底部边框
sns.despine(f, left=True, bottom=True)
# 绘制散点图，同时为不同的点指定颜色和大小
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)
plt.show()