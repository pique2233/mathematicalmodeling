import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# 示例 0-1 规划问题：最大化 c^T * x 约束 Ax <= b 和 x 是二进制变量

# 定义目标函数系数
c = [-1, -2]

# 定义约束矩阵和约束向量
A = [[2, 1], [1, 1]]
b = [20, 16]

# 定义边界
x0_bounds = (0, 1)
x1_bounds = (0, 1)

# 用 linprog 解决问题
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# 优化过程可视化 (Optimization Process Visualization)
iterations = np.arange(1, 11)
objective_values = -np.log(iterations + 1)  # 示例目标函数变化

plt.figure(figsize=(14, 7))
plt.plot(iterations, objective_values, marker='o', color='#1f77b4', markersize=8, linestyle='-', linewidth=2, label='Objective Value')
plt.title('Optimization Process Visualization', fontsize=18, fontweight='bold')
plt.xlabel('Iterations', fontsize=14)
plt.ylabel('Objective Function Value', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.show()

# 可行解空间图 (Feasible Region Plot)
x = np.linspace(0, 10, 200)
y1 = (b[0] - A[0][0] * x) / A[0][1]
y2 = (b[1] - A[1][0] * x) / A[1][1]

plt.figure(figsize=(14, 7))
plt.plot(x, y1, label=r'$2x_1 + x_2 \leq 20$', color='#ff7f0e', linewidth=2)
plt.plot(x, y2, label=r'$x_1 + x_2 \leq 16$', color='#2ca02c', linewidth=2)
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 > 0) & (y2 > 0), color='grey', alpha=0.3)
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.xlabel(r'$x_1$', fontsize=14)
plt.ylabel(r'$x_2$', fontsize=14)
plt.title('Feasible Region Plot', fontsize=18, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# 打印解
print(f"Optimal solution: {result.x}")
print(f"Objective function value: {result.fun}")