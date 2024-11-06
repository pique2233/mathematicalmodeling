# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(8, 6))
# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

# 加载示例数据集
dots = sns.load_dataset("dots")

# 创建一个名为"rocket_r"的调色板
palette = sns.color_palette("rocket_r")

# 绘制折现图
sns.relplot(
    data=dots,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建一个模拟数据集
np.random.seed(42)
time = np.tile(np.arange(0, 10), 20)
firing_rate = np.random.randn(200) * 10 + time * 3
coherence = np.random.choice(['low', 'medium', 'high'], size=200)
choice = np.random.choice(['T1', 'T2'], size=200)
align = np.random.choice(['left', 'right'], size=200)

# 创建 DataFrame
dots = pd.DataFrame({
    'time': time,
    'firing_rate': firing_rate,
    'coherence': coherence,
    'choice': choice,
    'align': align
})

# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

# 创建一个名为"rocket_r"的调色板
palette = sns.color_palette("rocket_r")

# 绘制折线图，使用 relplot 绘图，并设置图形大小
sns.relplot(
    data=dots,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=6, aspect=1.33,  # 直接设置图形大小
    facet_kws=dict(sharex=False),
)

# 显示图表
plt.show()