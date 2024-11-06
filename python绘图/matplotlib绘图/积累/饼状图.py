import matplotlib.pyplot as plt

# 数据
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]

# 设置颜色
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# 设置分离的距离
explode = (0, 0, 0, 0)  # 仅将第一个切片“爆炸”出来

# 创建饼状图
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# 设置饼状图的轴，使其均匀
plt.axis('equal')

# 显示图表
plt.title('Pie Chart Example')
plt.show()
"""labels 是饼状图的标签。
sizes 是每个部分的大小。
colors 是每个部分的颜色。
explode 设置了某些部分的分离距离，这里仅将第一个部分分离出来。
autopct 是显示每个部分的百分比。
shadow 设置了阴影效果。
startangle 设置了开始的角度。
"""
