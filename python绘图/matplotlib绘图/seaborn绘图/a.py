import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 生成样本数据
np.random.seed(42)
data = pd.DataFrame({
    'Category': np.repeat(['A', 'B', 'C', 'D'], 100),
    'Values': np.concatenate([
        np.random.normal(0, 1, 100),
        np.random.normal(5, 1.5, 100),
        np.random.normal(10, 1, 100),
        np.random.normal(15, 2, 100)
    ])
})

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制小提琴图
sns.violinplot(x='Category', y='Values', data=data, inner='box', palette='Set2', linewidth=1.5)

# 添加标题和标签
plt.title('Violin Plot with Box Plot Inside', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Values', fontsize=14)

# 显示图表
plt.show()

"""小提琴部分：
每个“提琴”的宽度表示数据的分布密度。宽的部分表示数据集中分布的区域，窄的部分表示数据较少的区域。比如，组1（左边第一组）的小提琴图在中间较宽，表示数据在中间值附近较为集中，而两端较窄，表示极端值较少。
箱线部分：
在小提琴内部，你可以看到一个箱线图。箱线图显示了数据的四分位范围（即中间50%的数据），中位数以粗线表示。上四分位数与下四分位数之间的距离反映了数据的离散程度。"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 生成样本数据
np.random.seed(10)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1.5, 100)
data3 = np.random.normal(-2, 0.5, 100)
data = [data1, data2, data3]

# 创建小提琴箱线图
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, inner="box", linewidth=1.5)

# 添加图像标题和标签
plt.title('Violin Plot Example', fontsize=16)
plt.xlabel('Groups', fontsize=14)
plt.ylabel('Values', fontsize=14)

# 显示图像
plt.show()
