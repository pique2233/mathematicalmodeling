# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))

# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 加载示例数据集
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

# 定义了一个包含要使用的网络的列表
used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
# 获取数据框的列名，并将其转换为整数类型、检查列名是否在used_networks列表中
used_columns = (df.columns
                  .get_level_values("network")
                  .astype(int)
                  .isin(used_networks))
# 根据used_columns筛选数据框
df = df.loc[:, used_columns]
# 将数据框的列名连接成一个字符串，用“-”分隔
df.columns = df.columns.map("-".join)

# 计算数据框的协方差矩阵，并将其转换为长格式
corr_mat = df.corr().stack().reset_index(name="correlation")

# 绘制散点热力图
g = sns.relplot(
    data=corr_mat,
    x="level_0", y="level_1", hue="correlation", size="correlation",
    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
    height=10, sizes=(50, 250), size_norm=(-.2, .8),
)

# 设置x轴和y轴的标签为空字符串，并调整图形的比例
g.set(xlabel="", ylabel="", aspect="equal")
# 移除左侧和下侧的轴线
g.despine(left=True, bottom=True)
# 设置轴线的边缘百分比
g.ax.margins(.02)
# 将x轴的标签旋转90度
for label in g.ax.get_xticklabels():
    label.set_rotation(90)
plt.show()