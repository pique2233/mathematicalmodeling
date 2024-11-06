import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建自定义数据集
data = {
    'category': ['A', 'B', 'C', 'D', 'E'],
    'total': [10, 15, 7, 25, 12],
    'alcohol': [5, 7, 3, 10, 4]
}
df = pd.DataFrame(data)

# 设置图大小
f, ax = plt.subplots(figsize=(8, 5))

# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 设置颜色代码为"pastel"并绘制第一个条形图
sns.set_color_codes("pastel")
sns.barplot(x="total", y="category", data=df,
            label="Total", color="b", edgecolor="w", linewidth=2)

# 设置颜色代码为"muted"并绘制第二个条形图
sns.set_color_codes("muted")
sns.barplot(x="alcohol", y="category", data=df,
            label="Alcohol-involved", color="b", edgecolor="w", linewidth=2)

# 添加图例
ax.legend(ncol=2, loc="lower right", frameon=True, fontsize=12)

# 设置x轴和y轴的范围和标签
ax.set(xlim=(0, 30), ylabel="Category",
       xlabel="Values")

# 移除左侧和底部边框
sns.despine(left=True, bottom=True)

# 设置标题
plt.title('Custom Data: Total vs Alcohol Involved', fontsize=16, fontweight='bold')

plt.show()