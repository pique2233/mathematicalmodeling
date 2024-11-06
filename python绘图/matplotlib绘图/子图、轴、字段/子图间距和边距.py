# 引入所需库
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


# 设置随机数种子
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

# 调整子图的布局，将底部边距设置为0.1，右侧边距设置为0.8，顶部边距设置为0.9
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
# 创建一个矩形区域，用于放置颜色图例
cax = plt.axes((0.85, 0.1, 0.075, 0.8))
# 在当前子图中添加一个颜色图例
plt.colorbar(cax=cax)

plt.show()