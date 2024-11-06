# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))
# 设置主题
sns.set_theme()

# 加载示例数据集
seaice = sns.load_dataset("seaice")
# 添加一个 decade 列来对数据进行分组
seaice["Decade"] = seaice["Date"].dt.year.round(-1)
# 绘制小提琴图
sns.violinplot(seaice, x="Extent", y="Decade", orient="y", fill=False)
plt.show()