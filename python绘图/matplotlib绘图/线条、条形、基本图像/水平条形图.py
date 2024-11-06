# 引入所需库
import matplotlib.pyplot as plt
import numpy as np

# 设置随机种子
np.random.seed(19680801)

# 定义数据
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()
# 绘制水平条形图
hbars = ax.barh(y_pos, performance, xerr=error, align='center')
# 设置y轴标签
ax.set_yticks(y_pos, labels=people)
# 反转y轴
ax.invert_yaxis()
# 设置x轴标签
ax.set_xlabel('Performance')
# 设置图表标题
ax.set_title('How fast do you want to go today?')

#  添加数据标签
ax.bar_label(hbars, fmt='%.2f')
# 设置x轴限制
ax.set_xlim(right=15)

plt.show()