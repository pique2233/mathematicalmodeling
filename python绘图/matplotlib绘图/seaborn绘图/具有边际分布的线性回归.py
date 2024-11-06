# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(6, 15))
# 将主题设置为暗色网格风格
sns.set_theme(style="darkgrid")

# 加载示例数据集
tips = sns.load_dataset("tips")
# 绘制散点图和线性回归拟合曲线
g = sns.jointplot(x="total_bill", y="tip", data=tips,
                  kind="reg", truncate=False,
                  xlim=(0, 60), ylim=(0, 12),
                  color="m", height=7)
plt.show()
