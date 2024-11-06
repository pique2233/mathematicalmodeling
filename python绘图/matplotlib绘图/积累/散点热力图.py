import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置图大小
f, ax = plt.subplots(figsize=(14, 12))

# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 自定义数据集，增加样本和特征数量，并增加随机性
np.random.seed(None)  # 移除固定的随机种子
num_samples = 1000
num_features = 20
data = {f'Feature{i+1}': np.random.randn(num_samples) + np.random.randn(1)[0] * 5 for i in range(num_features)}
df = pd.DataFrame(data)

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