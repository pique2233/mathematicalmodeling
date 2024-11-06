import matplotlib.pyplot as plt
import numpy as np

# 示例数据
categories = np.arange(0, 8)
values1 = np.array([3, 1, 2, 3, 2, 5, 7, 6])
values3 = np.array([2, 3, 4, 1, 4, 2, 5, 3])

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制上方的折线堆叠图，设置透明度和边缘线
plt.stackplot(categories, values1, labels=['Group 1', 'Group 2'],
              colors=['#1f77b4', '#ff7f0e'], alpha=0.6, edgecolor='grey', linewidth=1.5)

# 绘制下方的折线堆叠图，设置透明度和边缘线
plt.stackplot(categories, -values3, labels=['Group 3', 'Group 4'],
              colors=['#2ca02c', '#d62728'], alpha=0.6, edgecolor='grey', linewidth=1.5)

# 设置X轴范围，使最左边从0开始，最右边到达图像边界
plt.xlim(0, 7)

# 添加坐标轴标签和标题
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Stacked Area Plot Above and Below Axis')

# 显示图例
plt.legend(loc='upper left')

# 显示图表
plt.show()