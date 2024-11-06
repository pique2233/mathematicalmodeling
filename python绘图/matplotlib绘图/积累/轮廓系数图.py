import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples, silhouette_score

# 生成数据集
X, _ = make_blobs(n_samples=500, n_features=2, centers=4, cluster_std=1.0, random_state=42)

# KMeans 聚类
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# 散点图 (Scatter Plot)
plt.figure(figsize=(14, 7))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=300, alpha=0.6, marker='X')
plt.title('KMeans++ Clustering', fontsize=18, fontweight='bold')
plt.xlabel('Feature 1', fontsize=14)
plt.ylabel('Feature 2', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 肘部法则图 (Elbow Plot)
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(14, 7))
plt.plot(k_range, sse, marker='o', color='#1f77b4', linewidth=2, markersize=8)
plt.title('Elbow Method for Optimal K', fontsize=18, fontweight='bold')
plt.xlabel('Number of clusters (k)', fontsize=14)
plt.ylabel('Sum of Squared Errors (SSE)', fontsize=14)
plt.xticks(k_range, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 轮廓系数图 (Silhouette Plot)
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)
silhouette_vals = silhouette_samples(X, y_kmeans)

plt.figure(figsize=(14, 7))
y_lower, y_upper = 0, 0
for i, cluster in enumerate(np.unique(y_kmeans)):
    cluster_silhouette_vals = silhouette_vals[y_kmeans == cluster]
    cluster_silhouette_vals.sort()
    y_upper += len(cluster_silhouette_vals)
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_vals, alpha=0.7, label=f'Cluster {i+1}')
    y_lower += len(cluster_silhouette_vals)

plt.axvline(silhouette_score(X, y_kmeans), color='red', linestyle='--', linewidth=2)
plt.title('Silhouette Plot for KMeans++ Clustering', fontsize=18, fontweight='bold')
plt.xlabel('Silhouette Coefficient', fontsize=14)
plt.ylabel('Cluster', fontsize=14)
plt.yticks([])
plt.xticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
