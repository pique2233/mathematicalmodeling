# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))
# 设置主题
sns.set_theme()

# 加载示例数据集
flights_long = sns.load_dataset("flights")
# 重塑数据集
flights = (
    flights_long
    .pivot(index="month", columns="year", values="passengers")
)

#  绘制热力图
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
plt.show()