# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 创建数据
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
# 绘制棉棒图
plt.stem(x, y)
plt.show()