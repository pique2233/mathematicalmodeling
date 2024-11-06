# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

# 设置图大小
f, ax = plt.subplots(figsize=(6, 15))
# 将主题设置为白色网格风格
sns.set_theme()

#  创建一个示例数据集
r = np.linspace(0, 10, num=100)
df = pd.DataFrame({'r': r, 'slow': r, 'medium': 2 * r, 'fast': 4 * r})

#  重塑数据帧，以便将其转换为极坐标格式
df = pd.melt(df, id_vars=['r'], var_name='speed', value_name='theta')

# 创建散点图对象
g = sns.FacetGrid(df, col="speed", hue="speed",
                  subplot_kws=dict(projection='polar'), height=4.5,
                  sharex=False, sharey=False, despine=False)

#  在极坐标系中绘制散点图
g.map(sns.scatterplot, "theta", "r")

plt.show()
