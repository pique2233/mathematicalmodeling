# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib
matplotlib.use('TkAgg')

# 设置随机数种子
np.random.seed(19680801)
# 生成随机高斯混合模型的函数
def gaussian_mixture(x, n = 5):
    def add_random_gaussian(a):
        amplitude = 1 / (.1 + np.random.random())
        dx = x[-1] - x[0]
        x0 = (2 * np.random.random() - .5) * dx
        z = 10 / (.1 + np.random.random()) / dx
        a += amplitude * np.exp(-(z * (x - x0))**2)
    a = np.zeros_like(x)
    for j in range(n):
        add_random_gaussian(a)
    return a


x = np.linspace(0, 100, 101)
ys = [gaussian_mixture(x) for _ in range(3)]

fig, ax = plt.subplots()
# 绘制流图
ax.stackplot(x, ys, baseline='wiggle')
plt.show()