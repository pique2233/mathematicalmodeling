import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split

# 生成示例数据集
X, y = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 训练Fisher判别模型
lda = LDA()
lda.fit(X_train, y_train)

# 判别边界图 (Discriminant Boundary Plot)
plt.figure(figsize=(14, 7))
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = lda.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.coolwarm)
plt.title('Fisher Discriminant Analysis - Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()

# 散点图 (Scatter Plot) - Fisher判别方向上的投影
X_lda = lda.transform(X_train)
plt.figure(figsize=(14, 7))
plt.scatter(X_lda, np.zeros_like(X_lda), c=y_train, cmap=plt.cm.coolwarm, edgecolors='k')
plt.title('Fisher Discriminant Analysis - Projection')
plt.xlabel('Fisher Discriminant Axis')
plt.grid(True)
plt.show()

# 投影直方图 (Projection Histogram)
plt.figure(figsize=(14, 7))
plt.hist(X_lda[y_train == 0], bins=20, alpha=0.5, label='Class 0', color='blue')
plt.hist(X_lda[y_train == 1], bins=20, alpha=0.5, label='Class 1', color='red')
plt.title('Fisher Discriminant Analysis - Projection Histogram')
plt.xlabel('Fisher Discriminant Axis')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()