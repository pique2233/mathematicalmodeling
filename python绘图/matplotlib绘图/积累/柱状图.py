import numpy as np  # 只是辅助生成列表用的

import matplotlib.pyplot as plt
x = np.arange(3)
x1 = [79, 88, 80]
x2 = [80, 82, 83]

total_width, n = 0.6, 2
width = total_width / n
x = x - (total_width - width) / 2  # 现在的x是每个并列柱的第一柱的中心横坐标

plt.bar(x, x1, width=width, label='Boy')  # 图一
plt.bar(x + width, x2, width=width, label='Girl', fc='y')  # 图二
plt.xticks(np.arange(3), ['Chinese', 'Math', 'English'])  # 更改横轴标签
plt.legend()  # 添加图例
plt.title("Exam Result")
plt.show()
