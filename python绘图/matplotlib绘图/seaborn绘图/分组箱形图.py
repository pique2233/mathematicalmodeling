# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))

# 将主题设置为带有刻度的风格、绘图颜色方案为柔和色彩
sns.set_theme(style="ticks", palette="pastel")

# 加载示例数据集
tips = sns.load_dataset("tips")

# 绘制分组箱形图
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)
plt.show()