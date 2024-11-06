import numpy as np

# 初始化参数
num_centers = 5  # 配送中心数量
num_customers = 10  # 客户数量
cost_fixed = np.random.randint(10, 50, size=num_centers)  # 配送中心运营成本
locations_centers = np.random.rand(num_centers, 2)  # 配送中心位置
locations_customers = np.random.rand(num_customers, 2)  # 客户位置
c = 1  # 距离成本比例系数

# 计算距离矩阵
distance_matrix = np.linalg.norm(locations_centers[:, np.newaxis] - locations_customers, axis=2)

# 初始化遗传算法参数
population_size = 50
generations = 100
mutation_rate = 0.05


# 定义适应度函数
def fitness_function(individual):
    selected_centers = individual[:num_centers]
    customer_assignments = individual[num_centers:].reshape(num_centers, num_customers)
    total_cost = np.sum(cost_fixed * selected_centers)
    for i in range(num_centers):
        total_cost += np.sum(c * distance_matrix[i] * customer_assignments[i])
    return total_cost


# 初始化种群
population = np.random.randint(2, size=(population_size, num_centers + num_centers * num_customers))

# 遗传算法主循环
for generation in range(generations):
    # 计算种群适应度
    fitness_scores = np.array([fitness_function(ind) for ind in population])

    # 选择操作（轮盘赌）
    selected_indices = np.random.choice(np.arange(population_size), size=population_size,
                                        p=1 / fitness_scores / np.sum(1 / fitness_scores))
    selected_population = population[selected_indices]

    # 交叉操作
    offspring_population = []
    for i in range(0, population_size, 2):
        parent1 = selected_population[i]
        parent2 = selected_population[i + 1]
        crossover_point = np.random.randint(0, len(parent1))
        offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
        offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
        offspring_population.extend([offspring1, offspring2])

    # 变异操作
    offspring_population = np.array(offspring_population)
    mutation_mask = np.random.rand(*offspring_population.shape) < mutation_rate
    offspring_population[mutation_mask] = 1 - offspring_population[mutation_mask]

    # 更新种群
    population = offspring_population

# 选出适应度最好的个体
best_individual = population[np.argmin([fitness_function(ind) for ind in population])]

# 输出结果
selected_centers = best_individual[:num_centers]
customer_assignments = best_individual[num_centers:].reshape(num_centers, num_customers)
print(f"最优配送中心选择: {selected_centers}")
print(f"客户分配方案: {customer_assignments}")