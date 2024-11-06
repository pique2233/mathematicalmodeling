# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置图大小
f, ax = plt.subplots(figsize=(9, 6))
# 设置为白色网格主题
sns.set_theme(style="whitegrid")

# 生成示例数据
rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

# 绘制折线图
sns.lineplot(data=data, palette="tab10", linewidth=2.5)
plt.show()