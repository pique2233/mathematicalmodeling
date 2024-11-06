# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建自拟数据集
np.random.seed(42)
carat = np.random.uniform(0.2, 3.5, 1000)  # 生成随机carat值，范围在0.2到3.5之间
price = carat * (np.random.uniform(2000, 15000, size=1000) + np.random.normal(0, 1000, 1000))  # 价格与carat值正相关，加入一些噪声
clarity = np.random.choice(["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"], 1000)  # 随机生成清晰度
depth = np.random.uniform(20, 2000, 1000)  # 随机生成depth值，范围在45到70之间
#随机生成了一些数字
# 创建DataFrame
diamonds = pd.DataFrame({
    'carat': carat,
    'price': price,
    'clarity': clarity,
    'depth': depth
})

# 设置图大小
f, ax = plt.subplots(figsize=(6.5, 6.5))

# 移除图像的左部和底部边框
sns.despine(f, left=True, bottom=True)

# 定义清晰度的排序
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

# 绘制散点图，同时为不同的点指定颜色和大小
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(20,50 ), linewidth=0,
                data=diamonds, ax=ax)

# 显示图表
plt.show()
"""# 移除图像的左部和底部边框
sns.despine(f, left=True, bottom=True)
# 绘制散点图，同时为不同的点指定颜色和大小
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)
plt.show()"""

"""import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建自拟数据集
np.random.seed(42)
carat = np.random.uniform(0.2, 3.5, 1000)
price = carat * (np.random.uniform(2000, 15000, size=1000) + np.random.normal(0, 1000, 1000))
clarity = np.random.choice(["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"], 1000)
depth = np.random.uniform(20, 2000, 1000)

# 创建DataFrame
diamonds = pd.DataFrame({
    'carat': carat,
    'price': price,
    'clarity': clarity,
    'depth': depth
})

# 设置图大小
f, ax = plt.subplots(figsize=(8, 8))

# 移除图像的左部和底部边框
sns.despine(f, left=True, bottom=True)

# 定义清晰度的排序
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

# 绘制散点图，同时为不同的点指定颜色和大小
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.3,d=.5_r",
                hue_order=clarity_ranking,
                sizes=(50, 200), linewidth=0.5,
                data=diamonds, ax=ax)

# 设置标题
plt.title('Diamond Price vs Carat with Clarity and Depth', fontsize=16, fontweight='bold')

# 显示图表
plt.show()"""