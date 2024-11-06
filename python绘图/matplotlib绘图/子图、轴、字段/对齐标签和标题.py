# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 创建一个包含两个子图的图形
fig, axs = plt.subplots(2, 2, layout='constrained')

ax = axs[0][0]
ax.plot(np.arange(0, 1e6, 1000))
ax.set_title('Title0 0')
ax.set_ylabel('YLabel0 0')

ax = axs[0][1]
ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
ax.set_title('Title0 1')
ax.xaxis.tick_top()
ax.tick_params(axis='x', rotation=55)


for i in range(2):
    ax = axs[1][i]
    ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
    ax.set_ylabel('YLabel1 %d' % i)
    ax.set_xlabel('XLabel1 %d' % i)
    if i == 0:
        ax.tick_params(axis='x', rotation=55)

# 对图形的标签进行对齐
fig.align_labels()
# 对图形的标题进行对齐
fig.align_titles()

plt.show()