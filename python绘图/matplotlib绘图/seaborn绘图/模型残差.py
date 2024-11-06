# 引入所需库
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(6, 6))
# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

#  生成一些随机数据
rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

#  绘制散点图和线性回归拟合曲线
sns.residplot(x=x, y=y, lowess=True, color="g")
plt.show()