import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs

# 创建一个数据集
X, y = make_blobs(n_samples=100, centers=2, random_state=6)

# 创建SVM分类器并拟合数据
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X, y)

# 创建网格来绘制决策边界
xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 500),
                     np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 500))

# 计算决策边界
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 创建图形
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, levels=[Z.min(), 0, Z.max()], alpha=0.2, colors=['blue', 'red'])
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='black')

# 绘制数据点和支持向量
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap=plt.cm.coolwarm, edgecolors='k')
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')

# 添加标签和标题
plt.title('SVM Classification with Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()