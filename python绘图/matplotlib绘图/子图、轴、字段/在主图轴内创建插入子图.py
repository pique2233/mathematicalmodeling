# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)

"""
    定义时间间隔dt为0.001秒，生成一个从0开始，步长为dt，长度为10秒的时间序列t
    生成一个长度为1000的指数衰减函数r，用于模拟神经元的响应
    生成一个长度为len(t)的随机噪声序列x
    使用np.convolve()函数将x和r进行卷积运算，得到一个新的时间序列s，长度与x相同
"""
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

# 创建matplotlib图形对象fig和主轴main_ax，将t和s绘制在主轴上
fig, main_ax = plt.subplots()
main_ax.plot(t, s)

# 设置主轴的x轴和y轴范围，并添加x轴和y轴标签以及图表标题
main_ax.set_xlim(0, 1)
main_ax.set_ylim(1.1 * np.min(s), 2 * np.max(s))
main_ax.set_xlabel('time (s)')
main_ax.set_ylabel('current (nA)')
main_ax.set_title('Gaussian colored noise')

# 创建一个右插入轴right_inset_ax，用于绘制s的概率分布图
right_inset_ax = fig.add_axes([.65, .6, .2, .2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probability', xticks=[], yticks=[])

# 创建一个左插入轴left_inset_ax，用于绘制r的时域图
left_inset_ax = fig.add_axes([.2, .6, .2, .2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulse response', xlim=(0, .2), xticks=[], yticks=[])

plt.show()