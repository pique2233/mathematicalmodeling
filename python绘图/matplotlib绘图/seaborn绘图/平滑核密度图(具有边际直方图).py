# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(7, 6))
# 设置为白色主题
sns.set_theme(style="white")

# 加载示例数据集
df = sns.load_dataset("penguins")
# 绘制联合直方图
g = sns.JointGrid(data=df, x="body_mass_g", y="bill_depth_mm", space=0)
# 绘制联合密度估计
g.plot_joint(sns.kdeplot,
             fill=True, clip=((2200, 6800), (10, 25)),
             thresh=0, levels=100, cmap="rocket")
# 绘制边际直方图
g.plot_marginals(sns.histplot, color="#03051A", alpha=1, bins=25)
plt.show()