# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置图大小
f, ax = plt.subplots(figsize=(7, 5))
# 将主题设置为带有刻度的风格
sns.set_theme(style="ticks")

# 加载示例数据集
diamonds = sns.load_dataset("diamonds")

# 去除图像的边框
sns.despine(f)
# 绘制直方图、使用堆叠的方式显示分组(multiple="stack")
sns.histplot(
    diamonds,
    x="price", hue="cut",
    multiple="stack",
    palette="light:m_r",
    edgecolor=".3",
    linewidth=.5,
    log_scale=True,
)
# 将x轴的刻度标签更改为普通数字
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
# 设置x轴的刻度标签
ax.set_xticks([500, 1000, 2000, 5000, 10000])
plt.show()