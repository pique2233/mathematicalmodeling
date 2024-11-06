# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))

# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")
# 创建一个随机数生成器，并设置随机种子为11
rs = np.random.RandomState(11)
# 生成1000个服从Gamma分布的随机数，参数为2
x = rs.gamma(2, size=1000)
# 生成1000个服从正态分布的随机数，均值为0，方差为1，然后与Gamma分布的随机数相加
y = -.5 * x + rs.normal(size=1000)
# 绘制散点图，并使用hexbin图显示密度
sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")
plt.show()