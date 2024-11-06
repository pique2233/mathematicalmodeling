# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(6, 15))
# 将主题设置为白色风格
sns.set_theme(style="white")

# 加载示例数据集
mpg = sns.load_dataset("mpg")

#  绘制散点图
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)
plt.show()