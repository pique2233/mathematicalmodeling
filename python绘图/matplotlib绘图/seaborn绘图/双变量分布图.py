# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 设置图大小
f, ax = plt.subplots(figsize=(6, 6))
# 将主题设置为暗色风格
sns.set_theme(style="dark")

# 模拟来自双变量高斯的数据
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# 绘制了一个散点图
sns.scatterplot(x=x, y=y, s=5, color=".15")
# 绘制了一个直方图
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
# 绘制了一个核密度估计图
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

plt.show()