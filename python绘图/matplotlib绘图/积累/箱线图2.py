# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 手动创建数据集，模拟 "tips" 数据集
np.random.seed(42)
days = np.random.choice(["Thur", "Fri", "Sat", "Sun"], 200)
total_bill = np.random.normal(20, 8, 200)
smoker = np.random.choice(["Yes", "No"], 200)

# 创建DataFrame
tips = pd.DataFrame({
    "day": days,
    "total_bill": total_bill,
    "smoker": smoker
})

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))

# 将主题设置为带有刻度的风格、绘图颜色方案为柔和色彩
sns.set_theme(style="whitegrid", palette="pastel",context="notebook")
# 绘制分组箱形图
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)

# 移除图像的左部和底部边框
sns.despine(offset=10, trim=True)

# 显示图表
plt.show()