# 引入所需库
import seaborn as sns
import matplotlib.pyplot as plt

# 设置图大小
f, ax = plt.subplots(figsize=(8, 6))
# 将图像主题设置为暗网格主题
sns.set_theme(style="darkgrid")

#  加载示例数据集
fmri = sns.load_dataset("fmri")

# lineplot 默认带误差带
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
plt.show()