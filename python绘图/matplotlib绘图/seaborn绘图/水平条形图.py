# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(6, 15))
# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)

# 将颜色代码设置为"pastel"
sns.set_color_codes("pastel")
# 绘制第一个条形图
sns.barplot(x="total", y="abbrev", data=crashes,
            label="Total", color="b")

# 将颜色代码设置为"muted"
sns.set_color_codes("muted")
# 绘制第二个条形图
sns.barplot(x="alcohol", y="abbrev", data=crashes,
            label="Alcohol-involved", color="b")

# 添加图例
ax.legend(ncol=2, loc="lower right", frameon=True)
# 置x轴和y轴的范围和标签
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
# 将左侧和底部边框去除
sns.despine(left=True, bottom=True)

plt.show()