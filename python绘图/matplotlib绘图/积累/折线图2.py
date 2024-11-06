import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['PingFang HK']  # 使用 macOS 默认的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建折线图
plt.plot(x, y, color='blue', linestyle='--', linewidth=2, marker='o', markersize=6)

# 设置横纵坐标名称
plt.xlabel('X轴名称')
plt.ylabel('Y轴名称')

# 设置标题
plt.title('折线图示例')

# 设置背景颜色
plt.gca().set_facecolor('none')

# 设置网格线
plt.grid(False,linestyle=':', color='gray', alpha=0.7)
# 设置边框
plt.gca().spines['top'].set_visible(False)  # 隐藏上边框
plt.gca().spines['right'].set_visible(False)  # 隐藏右边框
plt.gca().spines['right'].set_visible(False)

# 显示图像
plt.show()