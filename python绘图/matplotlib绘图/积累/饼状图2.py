import matplotlib.pyplot as plt

# 数据
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]

# 设置颜色
colors = ['#6a2c70','#b83b5e','#f08a5d','#f9ed69']

# 设置分离的距离
explode = (0.1, 0, 0, 0)  # 仅将第一个切片“爆炸”出来

# 创建饼状图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                  autopct='%1.1f%%', shadow=True, startangle=140,
                                  wedgeprops=dict(edgecolor='w', linewidth=2))

# 设置文本和自动文本的字体属性
plt.setp(texts, size=12, weight="bold", color='darkblue')
plt.setp(autotexts, size=10, weight="bold", color='white')

# 添加中心空白
centre_circle = plt.Circle((0,0),0.40,fc='white', linewidth=1.5)
fig.gca().add_artist(centre_circle)

# 确保饼图是圆的
ax.axis('equal')

# 添加图例
ax.legend(wedges, labels,
          title="Categories",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=10)

# 添加标题
plt.title('Pie Chart with Enhanced Aesthetics', fontsize=16, fontweight='bold')

# 显示图表
plt.show()
