# 引入所需库
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib
matplotlib.use('TkAgg')


# 创建数据
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    'Africa': [.228, .284, .365, .477, .631, .814, 1.044, 1.275],
    'the Americas': [.340, .425, .519, .619, .727, .840, .943, 1.006],
    'Asia': [1.394, 1.686, 2.120, 2.625, 3.202, 3.714, 4.169, 4.560],
    'Europe': [.220, .253, .276, .295, .310, .303, .294, .293],
    'Oceania': [.012, .015, .019, .022, .026, .031, .036, .039],
}

fig, ax = plt.subplots()
# 绘制堆叠图
ax.stackplot(year, population_by_continent.values(),
             labels=population_by_continent.keys(), alpha=0.8)
# 添加图例
ax.legend(loc='upper left', reverse=True)
# 设置标题和轴标签
ax.set_title('World population')
ax.set_xlabel('Year')
ax.set_ylabel('Number of people (billions)')
# 设置刻度
ax.yaxis.set_minor_locator(mticker.MultipleLocator(.2))

plt.show()