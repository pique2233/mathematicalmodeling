# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import matplotlib
matplotlib.use('TkAgg')

#定义了一个名为SUCCESS_SYMBOLS的列表
SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]
# 设置了随机数种子，生成了25个模拟数据点，并设置了这些数据点的技能值、起飞角度、推力和成功状态
# 创建了一个名为data的zip对象，将技能值、起飞角度、推力和成功状态组合在一起
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)

# 创建了一个名为cmap的颜色映射，用于将推力值映射到颜色
cmap = plt.colormaps["plasma"]
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
# 遍历data中的每个数据点，根据技能值和起飞角度计算变换矩阵t，然后根据成功状态选择相应的标记符号m，最后将标记符号添加到图形中。

for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
# 添加了一个颜色图例，用于解释推力值的颜色映射
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
# 设置了x轴和y轴的标签
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")

plt.show()