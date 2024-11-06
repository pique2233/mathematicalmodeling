import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成示例数据集
np.random.seed(42)
data = pd.DataFrame({
    'value': np.random.normal(size=500),
    'category': np.random.choice(['A', 'B', 'C', 'D', 'E'], size=500)
})

# 设置图大小
plt.figure(figsize=(8, 8))
# 将主题设置为白色网格风格
sns.set_theme(style="whitegrid")

# 绘制条件核密度曲线图
sns.kdeplot(
    data=data,
    x="value", hue="category",
    multiple="fill", clip=(-3, 3),
    palette="ch:rot=-.25,hue=1,light=.75",
)

plt.title('Conditional KDE Plot with Custom Data')
plt.show()

