# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))
# 将主题设置为白色网格的风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
diamonds = sns.load_dataset("diamonds")
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

# 绘制密度分布图，使用 width_method 参数指定了宽度计算方法为linear
sns.boxenplot(
    diamonds, x="clarity", y="carat",
    color="b", order=clarity_ranking, width_method="linear",
)
plt.show()