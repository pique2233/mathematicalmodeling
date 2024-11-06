# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt


# 设置图大小
f, ax = plt.subplots(figsize=(6, 6))
# 将主题设置为白色风格，使用预定义的颜色代码
sns.set_theme(style="white", color_codes=True)

# 加载示例数据集
mpg = sns.load_dataset("mpg")

# 创建一个联合散点图对象
g = sns.JointGrid(data=mpg, x="mpg", y="acceleration", space=0, ratio=17)
# 绘制联合散点图
g.plot_joint(sns.scatterplot, size=mpg["horsepower"], sizes=(30, 120),
             color="g", alpha=.6, legend=False)
# 绘制边缘散点图
g.plot_marginals(sns.rugplot, height=1, color="g", alpha=.6)
plt.show()