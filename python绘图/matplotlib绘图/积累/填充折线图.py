import matplotlib.pyplot as plt
import numpy as np

# 设置风格为 ggplot
plt.style.use('ggplot')

# 生成数据
np.random.seed(1)
x = np.linspace(0, 8, 16)
y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))

# 创建图形和轴对象
fig, ax = plt.subplots(figsize=(10, 6))

# 填充两条折线之间的区域
ax.fill_between(x, y1, y2, alpha=0.2,color='skyblue', label='Fill between y1 and y2')

# 绘制两条折线的平均值曲线
ax.plot(x, (y1 + y2)/2, color='darkblue', linewidth=2, linestyle='-', label='Average of y1 and y2')

# 设置坐标轴的范围和刻度
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_xticks(np.arange(0, 9, 1))
ax.set_yticks(np.arange(0, 9, 1))

# 添加网格
ax.grid(True, which='both', linestyle='--', linewidth=0.7, color='gray', alpha=0.7)

# 设置标题和标签
ax.set_title('Filled Line Plot Example', fontsize=16, fontweight='bold')
ax.set_xlabel('X Axis Label', fontsize=14)
ax.set_ylabel('Y Axis Label', fontsize=14)
plt.gca().set_facecolor('white')
# 添加图例
ax.legend(loc='upper left', fontsize=12)

# 展示图形
plt.show()