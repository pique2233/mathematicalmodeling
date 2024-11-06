# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))

# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

# 加载示例数据集
penguins = sns.load_dataset("penguins")

# 绘制核密度估计图
g = sns.jointplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    kind="kde",
)
plt.show()