"""import matplotlib.pyplot as plt
import numpy as np

# 数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x) / 4  # 限制tan(x)的范围，使其更适合展示"""
"""marker 参数用于控制数据点的标记样式。以下是一些常用的 marker 样式：

	•	’.’：点标记
	•	’,’：像素点
	•	‘o’：圆圈
	•	‘v’：下三角形
	•	’^’：上三角形
	•	’<’：左三角形
	•	’>’：右三角形
	•	‘1’：下部花瓣
	•	‘2’：上部花瓣
	•	‘3’：左部花瓣
	•	‘4’：右部花瓣
	•	‘s’：正方形
	•	‘p’：五边形（实心五角星）
	•	’*’：星形
	•	‘h’：六边形1
	•	‘H’：六边形2
	•	’+’：加号
	•	‘x’：x号
	•	‘D’：菱形
	•	‘d’：窄菱形
	•	’|’：垂直线
	•	’_’：水平线"""
# 创建折线图 尺寸
"""
plt.figure(figsize=(12, 8))
plt.plot(x, y1, marker='o', label='sin(x)', color='dodgerblue', linewidth=2,markerfacecolor='red',markeredgecolor='blue',antialiased=True)
plt.plot(x, y2, marker='s', label='cos(x)', color='darkorange', linewidth=2, linestyle='--')
plt.plot(x, y3, marker='p', label='tan(x)/4', color='forestgreen', linewidth=2, linestyle=':')
#plt.bar(x,y1,color='skyblue')
for i in range(len(x)):
    plt.text(x[i], y1[i], f'({x[i]}, {y1[i]:.2f})', fontsize=10, ha='right', va='bottom')

# 添加标题和标签
plt.title('Trigonometric Functions at Discrete Points', fontsize=16, fontweight='bold')
plt.xlabel('X Axis', fontsize=14)
plt.ylabel('Y Axis', fontsize=14)

# 显示图例
plt.legend(loc='upper right', fontsize=12)

# 添加网格
plt.grid(True, which='major', linestyle='-.', linewidth=0.7,color='red')"""
"""which 参数：

	•	‘both’：网格线应用于主刻度和次刻度。
	•	‘major’：网格线仅应用于主刻度（通常是较长的刻度线）。
	•	‘minor’：网格线仅应用于次刻度（通常是较短的刻度线）。

linestyle 参数：
linestyle 控制网格线的样式。以下是常见的样式选项：

	•	’-’ 或 ‘solid’：实线。
	•	’–’ 或 ‘dashed’：虚线。
	•	’-.’ 或 ‘dashdot’：点划线。
	•	’:’ 或 ‘dotted’：点线。
"""
"""
plt.gca().spines['top'].set_visible(False)  # 隐藏上边框
plt.gca().spines['right'].set_visible(False)  # 隐藏右边框
# 限制y轴范围以避免tan(x)过大
plt.ylim(-2, 2)

# 显示图形
plt.show()"""
import matplotlib.pyplot as plt
import numpy as np

# 数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x) / 4  # 限制tan(x)的范围，使其更适合展示

# 创建折线图 尺寸
plt.figure(figsize=(12, 8))
plt.plot(x, y1, marker='o', label='sin(x)', color='#1f77b4', linewidth=2, markerfacecolor='#ff7f0e', markeredgecolor='#1f77b4', antialiased=True)
plt.plot(x, y2, marker='s', label='cos(x)', color='#2ca02c', linewidth=2, linestyle='--')
plt.plot(x, y3, marker='p', label='tan(x)/4', color='#d62728', linewidth=2, linestyle=':')

# 在数据点上添加标签
for i in range(len(x)):
    plt.text(x[i], y1[i], f'({x[i]}, {y1[i]:.2f})', fontsize=10, ha='right', va='bottom', color='#1f77b4')

# 添加标题和标签
plt.title('Trigonometric Functions at Discrete Points', fontsize=16, fontweight='bold')
plt.xlabel('X Axis', fontsize=14)
plt.ylabel('Y Axis', fontsize=14)

# 显示图例
plt.legend(loc='upper right', fontsize=12)

# 添加网格
plt.grid(True, which='major', linestyle='-.', linewidth=0.7, color='#c7c7c7')
plt.gca().set_facecolor('#f0f0f0')
plt.errorbar(x, y1, yerr=0.1, fmt='o', ecolor='black', capsize=5, elinewidth=2)
# 隐藏上、右边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 限制y轴范围以避免tan(x)过大
plt.ylim(-2, 2)

# 显示图形
plt.show()




