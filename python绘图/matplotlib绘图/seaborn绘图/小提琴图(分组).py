# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))

# 设置主题样式为暗色
sns.set_theme(style="dark")

# 加载示例数据集
tips = sns.load_dataset("tips")

# 分组小提琴图
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker",
               split=True, inner="quart", fill=False,
               palette={"Yes": "g", "No": ".35"})
plt.show()