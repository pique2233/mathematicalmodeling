# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('TkAgg')


# 读取图像
im = Image.open('cat.jpg')

fig, ax = plt.subplots()

# 设置随机数种子
np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()

# 添加水印
fig.figimage(im, 25, 25, zorder=3, alpha=.7)

plt.show()