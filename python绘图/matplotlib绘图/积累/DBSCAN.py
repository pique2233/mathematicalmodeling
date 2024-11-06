import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN

# 生成示例数据集
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=42)

# 训练DBSCAN模型
db = DBSCAN(eps=0.3, min_samples=5).fit(X)
labels = db.labels_

# 聚类结果图 (Cluster Result Plot)
plt.figure(figsize=(14, 7))
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1]  # 黑色用于噪声点
    class_member_mask = (labels == k)
    xy = X[class_member_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=10)
plt.title('DBSCAN Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()

# k-距离图 (k-distance Plot)
neighbors = NearestNeighbors(n_neighbors=4)
neighbors_fit = neighbors.fit(X)
distances, indices = neighbors_fit.kneighbors(X)
distances = np.sort(distances[:, 3], axis=0)

plt.figure(figsize=(14, 7))
plt.plot(distances)
plt.title('k-distance Plot for DBSCAN')
plt.xlabel('Data Points sorted by distance')
plt.ylabel('k-distance (4th Nearest Neighbor)')
plt.grid(True)
plt.show()