import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建一个模拟数据集
np.random.seed(41)
time = np.tile(np.arange(0, 10), 20)
firing_rate = np.random.randn(200) * 10 + time * 3
coherence = np.random.choice(['low', 'medium', 'high'], size=200)
choice = np.random.choice(['T1', 'T2'], size=200)
align = np.random.choice(['left', 'right'], size=200)

# 创建DataFrame
data = pd.DataFrame({
    'time': time,
    'firing_rate': firing_rate,
    'coherence': coherence,
    'choice': choice,
    'align': align
})

# 设置图大小
f, ax = plt.subplots(figsize=(8, 6))
sns.set_theme(style="ticks")

# 创建一个名为"rocket_r"的调色板
palette = sns.color_palette("rocket_r")

# 绘制折现图
sns.relplot(
    data=data,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)

plt.show()