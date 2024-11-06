# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
from string import ascii_letters
import numpy as np
import pandas as pd

# 设置图大小
f, ax = plt.subplots(figsize=(11, 9))
# 将主题设置为白色风格
sns.set_theme(style="white")

# 创建随机数据集
rs = np.random.RandomState(33)
d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                 columns=list(ascii_letters[26:]))

# 计算相关矩阵
corr = d.corr()

# 为上部三角生成遮罩
mask = np.triu(np.ones_like(corr, dtype=bool))

# 定义热力图的颜色映射
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# 绘制热力图
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()