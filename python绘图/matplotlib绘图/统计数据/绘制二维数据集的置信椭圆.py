# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import matplotlib
matplotlib.use('TkAgg')

# 此函数绘制给定数组变量 x 和 y 的协方差的置信椭圆
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    :param x: 输入数据，表示椭圆中心点的横坐标
    :param y: 输入数据，表示椭圆中心点的纵坐标
    :param ax: 绘图对象，用于在给定的坐标轴上绘制椭圆
    :param n_std: 标准差倍数，用于确定椭圆的半径
    :param facecolor: 图表背景颜色
    :param kwargs: 其他参数
    :return: matplotlib.patches.Ellipse对象
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])

    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)


    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

# 创建具有指定二维平均值(mu)和维度(scale)的随机二维数据集
# 相关性可以通过参数dependency控制
def get_correlated_dataset(n, dependency, mu, scale):
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]


# 设置随机数种子
np.random.seed(0)
# 定义PARAMETERS字典，包含三个键值对，分别表示正相关、负相关和弱相关
PARAMETERS = {
    'Positive correlation': [[0.85, 0.35],
                             [0.15, -0.65]],
    'Negative correlation': [[0.9, -0.4],
                             [0.1, -0.6]],
    'Weak correlation': [[1, 0],
                         [0, 1]],
}
# 定义二维平均值(mu)和维度(scale)
mu = 2, 4
scale = 3, 5

fig, axs = plt.subplots(1, 3, figsize=(9, 3))
# 循环遍历PARAMETERS字典的键值对
for ax, (title, dependency) in zip(axs, PARAMETERS.items()):
    # 生成一个具有给定相关性的数据集
    x, y = get_correlated_dataset(800, dependency, mu, scale)
    # 绘制散点图
    ax.scatter(x, y, s=0.5)
    # 绘制坐标轴上的辅助线
    ax.axvline(c='grey', lw=1)
    ax.axhline(c='grey', lw=1)
    # 绘制数据集的置信椭圆
    confidence_ellipse(x, y, ax, edgecolor='red')
    # 在子图上绘制均值点
    ax.scatter(mu[0], mu[1], c='red', s=3)
    # 设置子图标题
    ax.set_title(title)

plt.show()