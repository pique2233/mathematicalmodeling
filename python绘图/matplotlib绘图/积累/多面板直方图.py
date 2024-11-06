import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建自定义数据集
np.random.seed(42)
data = {
    'flipper_length_mm': np.random.normal(200, 30, 300),
    'species': np.random.choice(['Adelie', 'Chinstrap', 'Gentoo'], 300),
    'sex': np.random.choice(['Male', 'Female'], 300)
}
df = pd.DataFrame(data)

# 设置图大小
f, ax = plt.subplots(figsize=(8, 6))
# 将图像主题设置为暗网格主题
sns.set_theme(style="darkgrid")

# 绘制多面板直方图
sns.displot(
    df, x="flipper_length_mm", col="species", row="sex",
    binwidth=5, height=3, facet_kws=dict(margin_titles=True),
)
plt.show()