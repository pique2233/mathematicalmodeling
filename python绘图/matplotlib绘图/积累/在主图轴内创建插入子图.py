import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)

# 数据生成
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

# 创建主图
fig, main_ax = plt.subplots(figsize=(10, 6))
main_ax.plot(t, s, color='dodgerblue', linewidth=1)

# 设置主图的轴和标题
main_ax.set_xlim(0, 1)
main_ax.set_ylim(1.1 * np.min(s), 2 * np.max(s))
main_ax.set_xlabel('Time (s)', fontsize=12)
main_ax.set_ylabel('Current (nA)', fontsize=12)
main_ax.set_title('Gaussian Colored Noise', fontsize=16, fontweight='bold')

# 美化右插图 - 概率分布
right_inset_ax = fig.add_axes([.65, .6, .25, .25], facecolor='whitesmoke')
right_inset_ax.hist(s, bins=400, density=True, color='darkorange', alpha=0.7)
right_inset_ax.set_title('Probability Distribution', fontsize=10, color='darkorange')
right_inset_ax.set_xticks([])
right_inset_ax.set_yticks([])

# 美化左插图 - 脉冲响应
left_inset_ax = fig.add_axes([.15, .6, .25, .25], facecolor='whitesmoke')
left_inset_ax.plot(t[:len(r)], r, color='seagreen', linewidth=2)
left_inset_ax.set_title('Impulse Response', fontsize=10, color='seagreen')
left_inset_ax.set_xlim(0, .2)
left_inset_ax.set_xticks([])
left_inset_ax.set_yticks([])

plt.show()