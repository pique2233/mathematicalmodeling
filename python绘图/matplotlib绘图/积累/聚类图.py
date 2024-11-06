from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.normal(size=(10, 5))  # 随机生成10个样本，5个指标的数据，进行Q型层次聚类
labels = np.arange(10)  # 样本标签

plt.figure(figsize=(5, 5))  # 画布大小
Z = hierarchy.linkage(y=data1, method='weighted', metric='euclidean')  # 生成聚类树
hierarchy.dendrogram(Z, labels=labels)  # 画聚类树
plt.xlabel('x Axis', fontsize=10)
plt.ylabel('Y Axis', fontsize=10)
plt.title("title",fontsize=10)
plt.show()
