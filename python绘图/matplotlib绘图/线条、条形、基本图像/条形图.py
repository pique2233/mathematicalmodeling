# 引入所需库
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 定义数据
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# 绘制条形图
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# 添加图例
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()