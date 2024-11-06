# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
from string import ascii_letters
import numpy as np
import pandas as pd

# 设置图大小
f, ax = plt.subplots(figsize=(11, 9))
# 将主题设置为白色风格
sns.set_theme(style="ticks")

# 创建随机数据集
rs = np.random.RandomState(33)
d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                 columns=list(ascii_letters[26:]))

# 计算相关矩阵
corr = d.corr()

# 为上部三角生成遮罩
mask = np.triu(np.ones_like(corr, dtype=bool))

# 定义热力图的颜色映射
#cmap = sns.diverging_palette(230, 20, as_cmap=True)
cmap = sns.light_palette("#b83b5e", as_cmap=True)#配色自己找喜欢的配色



# 绘制热力图
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
         square=True, linewidths=.5, cbar_kws={"shrink": .5})
#sns.heatmap(corr, cmap=cmap, cbar_kws={"orientation": "horizontal", "label": "Correlation"})
#颜色条的方向。
#添加单元格标签以显示具体的数值：
#sns.heatmap(corr, cmap=cmap, annot=True, fmt=".2f")
#改变单元格之间的线宽和颜色sns.heatmap(corr, cmap=cmap, linewidths=1, linecolor='black')



plt.show()

"""sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, linecolor='black', annot=True, fmt=".2f",
            cbar_kws={"shrink": .5, "orientation": "horizontal", "label": "Correlation",
                      "aspect": 30, "pad": 0.1})shrink: 颜色条缩小到原始大小的50%。
orientation: 颜色条水平放置。
label: 为颜色条添加标签“Correlation”。
aspect: 设置颜色条的长宽比为30。
pad: 设置颜色条与主图之间的间距为0.1。"""