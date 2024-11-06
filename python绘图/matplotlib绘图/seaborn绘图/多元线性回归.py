import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建自定义数据集
np.random.seed(42)
data = {
    "total_bill": np.random.uniform(10, 50, 200),  # 随机生成200个账单金额
    "tip": np.random.uniform(1, 10, 200),  # 随机生成200个小费金额
    "sex": np.random.choice(["Male", "Female"], 200)  # 随机生成200个性别数据
}
custom_data = pd.DataFrame(data)

sns.set_theme(style="whitegrid")  # 使用白色网格主题

# 绘制散点图和回归曲线
plt.figure(figsize=(8, 6))
sns.regplot(
    data=custom_data,
    x="total_bill", y="tip",
    scatter_kws={'s': 50, 'alpha': 0.5},  # 散点的样式
    line_kws={'color': 'red', 'linewidth': 2}  # 回归线的样式
)

# 设置坐标轴标签
plt.xlabel("Total Bill (USD)", fontsize=12)
plt.ylabel("Tip (USD)", fontsize=12)

# 设置图形标题
plt.title("Total Bill vs Tip with Regression Line (Custom Data)", fontsize=16, fontweight='bold')

# 显示图表
plt.show()