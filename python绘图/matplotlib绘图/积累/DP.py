import matplotlib.pyplot as plt
import networkx as nx
import  numpy as np

# 1. 状态转移图 (State Transition Diagram)
plt.figure(figsize=(8, 6))
G = nx.DiGraph()
states = ['F(n-2)', 'F(n-1)', 'F(n)']
G.add_edges_from([('F(n-2)', 'F(n-1)'), ('F(n-1)', 'F(n)')])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=15, font_weight='bold', arrowsize=20)
plt.title("State Transition Diagram")
plt.show()

# 2. 最优解路径图 (Optimal Path Visualization)
plt.figure(figsize=(8, 8))
grid = np.array([[3, 2, 1, 3],
                 [4, 8, 2, 1],
                 [1, 5, 3, 2],
                 [6, 2, 9, 5]])

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        plt.text(j, i, grid[i, j], ha='center', va='center', fontsize=20)

path = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
for k in range(len(path) - 1):
    plt.arrow(path[k][1], path[k][0], path[k+1][1] - path[k][1], path[k+1][0] - path[k][0],
              head_width=0.2, head_length=0.2, fc='red', ec='red')

plt.xlim(-0.5, 3.5)
plt.ylim(3.5, -0.5)
plt.grid(True)
plt.title("Optimal Path Visualization")
plt.show()

# 3. 递归树 (Recursion Tree)
plt.figure(figsize=(8, 6))
G = nx.DiGraph()
nodes = [('F(4)', 'F(3)'), ('F(4)', 'F(2)'), ('F(3)', 'F(2)'), ('F(3)', 'F(1)'),
         ('F(2)', 'F(1)'), ('F(2)', 'F(0)')]
G.add_edges_from(nodes)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgreen', font_size=15, font_weight='bold', arrowsize=20)
plt.title("Recursion Tree")
plt.show()