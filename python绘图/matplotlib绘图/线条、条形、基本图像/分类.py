# 引入所需库
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
# 创建数据
data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
# 绘制柱状图
axs[0].bar(names, values)
# 绘制散点图
axs[1].scatter(names, values)
# 绘制折线图
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.show()