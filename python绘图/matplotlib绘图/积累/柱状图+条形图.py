import matplotlib.pyplot as plt
import numpy as np

# 示例数据
categories = ['A', 'B', 'C', 'D', 'E']
bar_values = [5, 7, 9, 4, 6]

# 创建条形图
plt.bar(categories, bar_values, color='skyblue')

# 添加折线图
plt.plot(categories, bar_values, marker='o', color='orange')

# 添加标注（可选）
for i in range(len(categories)):
    plt.text(i, bar_values[i] + 0.3, str(bar_values[i]), ha='center')

# 显示图形
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Line Plot')
plt.show()