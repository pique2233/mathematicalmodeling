# 引入所需库
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import matplotlib
matplotlib.use('TkAgg')

# 读取谷歌公司的股票价格数据，并计算股票价格的日变化率
price_data = cbook.get_sample_data('goog.npz')['price_data']
price_data = price_data[-250:]  # get the most recent 250 trading days
delta1 = np.diff(price_data["adj_close"]) / price_data["adj_close"][:-1]

# 价格数据（price_data）中的"volume"和"close"列进行某种计算，并将结果存储在变量"volume"和"close"中
volume = (15 * price_data["volume"][:-2] / price_data["volume"][0])**2
close = 0.003 * price_data["close"][:-2] / 0.003 * price_data["open"][:-2]

fig, ax = plt.subplots()
# 绘制散点图，其中颜色映射为收盘价，大小映射为成交量
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)
# 设置坐标轴标签和标题
ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')
# 添加颜色条
ax.grid(True)
# 调整子图布局
fig.tight_layout()

plt.show()