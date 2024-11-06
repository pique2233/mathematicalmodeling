# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 生成二维网格
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
# 定义数据列表
data = [(-1.5, .5, -6, -6),
        (1, -1, -46, 46),
        (-3, -1, 11, -11),
        (1, 1.5, 80, 80),
        (0.5, 0.25, 25, 15),
        (-1.5, -0.5, -5, 40)]
# 转换为numpy数组
data = np.array(data, dtype=[('x', np.float32), ('y', np.float32),
                             ('u', np.float32), ('v', np.float32)])
# 创建 2x2 子图
fig1, axs1 = plt.subplots(nrows=2, ncols=2)

"""
第一个子图（axs1[0, 0]）：使用默认的参数绘制barbs
第二个子图（axs1[0, 1]）：使用自定义的参数绘制barbs。这里使用了length=8，pivot='middle'等参数来调整barbs的长度和旋转角度
第三个子图（axs1[1, 0]）：使用自定义的参数绘制barbs。这里使用了fill_empty=True，rounding=False等参数来填充空心barbs，并调整其形状
第四个子图（axs1[1, 1]）：使用自定义的参数绘制barbs。这里使用了flagcolor='r'，barbcolor=['b', 'g']等参数来设置barbs的颜色，以及flip_barb=True来翻转barbs的方向
"""
axs1[0, 0].barbs(X, Y, U, V)
axs1[0, 1].barbs(
    data['x'], data['y'], data['u'], data['v'], length=8, pivot='middle')
axs1[1, 0].barbs(
    X, Y, U, V, np.sqrt(U ** 2 + V ** 2), fill_empty=True, rounding=False,
    sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3))
axs1[1, 1].barbs(data['x'], data['y'], data['u'], data['v'], flagcolor='r',
                 barbcolor=['b', 'g'], flip_barb=True,
                 barb_increments=dict(half=10, full=20, flag=100))

masked_u = np.ma.masked_array(data['u'])
masked_u[4] = 1000
masked_u[4] = np.ma.masked

plt.show()