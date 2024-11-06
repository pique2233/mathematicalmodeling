# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 创建一个矩阵
a = np.diag(range(15))
# 绘制矩阵
plt.matshow(a)

plt.show()