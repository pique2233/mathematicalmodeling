# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))

# 加载示例数据集
penguins = sns.load_dataset("penguins")

# 绘制条形图
g = sns.catplot(
    data=penguins, kind="bar",
    x="species", y="body_mass_g", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
# 删除左侧轴线
g.despine(left=True)
# 设置x轴和y轴的标签
g.set_axis_labels("", "Body mass (g)")
# 设置图例的标题为空
g.legend.set_title("")
plt.show()