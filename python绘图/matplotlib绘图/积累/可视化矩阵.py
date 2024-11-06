import matplotlib.pyplot as plt
import numpy as np
"""fig = plt.figure()

gs = plt.GridSpec(2, 2, width_ratios=[15, 1], height_ratios=[1, 1])

plt.subplot(gs[0, 0])
plt.title("A")
im = plt.pcolormesh(np.random.rand(10,20))
plt.axis('off')

plt.subplot(gs[1, 0])
plt.title("B")
im = plt.pcolormesh(np.random.rand(10,20))
plt.axis('off')

ax = plt.subplot(gs[:, 1])
fig.colorbar(im, cax=ax)
plt.show()"""

X=np.array([[0,3,2,4],[5,4,7,8],[9,16,8,5],[13,3,4,16],[6,18,1,20]])
A = np.arange(0, 100).reshape(10, 10)
ax = plt.matshow(X)
plt.colorbar(ax.colorbar, fraction=0.025)
plt.title("matrix X");
plt.show()

