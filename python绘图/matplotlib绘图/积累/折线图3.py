import matplotlib.pyplot as plt
import numpy as np

# 数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x) / 4  # 限制tan(x)的范围，使其更适合展示

# 创建折线图 尺寸
plt.figure(figsize=(12, 8))
plt.plot(x, y1, marker='o', label='sin(x)', color='dodgerblue', linewidth=2,
         markerfacecolor='red', markeredgecolor='blue', antialiased=True)
plt.plot(x, y2, marker='s', label='cos(x)', color='darkorange', linewidth=2, linestyle='--')
plt.plot(x, y3, marker='p', label='tan(x)/4', color='forestgreen', linewidth=2, linestyle=':')

# 为sin(x)的折点添加文字描述
for i in range(len(x)):
    plt.text(x[i], y1[i], f'({x[i]}, {y1[i]:.2f})', fontsize=10, ha='right', va='bottom')

# 添加标题和标签
plt.title('Trigonometric Functions at Discrete Points', fontsize=16, fontweight='bold')
plt.xlabel('X Axis', fontsize=14)
plt.ylabel('Y Axis', fontsize=14)

# 显示图例
plt.legend(loc='upper right', fontsize=12)

# 添加网格
plt.grid(True, which='major', linestyle='-.', linewidth=0.5, color='red')

plt.gca().spines['top'].set_visible(False)  # 隐藏上边框
plt.gca().spines['right'].set_visible(False)  # 隐藏右边框

# 限制y轴范围以避免tan(x)过大
plt.ylim(-2, 2)

# 显示图形
plt.show()