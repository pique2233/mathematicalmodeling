# 引入所需库
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


# 饼图的不同标签和对应大小
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()
# 定义explode元组，用于在饼图中突出显示特定部分
explode = (0, 0.1, 0, 0)
# 设置hatch列表，包含了饼图每个部分的填充样式(colors就会被覆盖)
# 设置shadow，表示是否需要为饼图添加阴影
# 设置startangle参数，使饼图从90度开始
# 设置textprops参数，调整饼图中文本的样式
# 设置radius参数，调整饼图的大小
ax.pie(sizes, explode=explode, labels=labels,
       # colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown'],
       hatch=['**O', 'oO', 'O.O', '.||.'],
       shadow=True, startangle=90,
       textprops={'size': 'smaller'}, radius=0.5)
plt.show()