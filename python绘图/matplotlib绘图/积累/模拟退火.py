import numpy as np
import pandas as pd
import os

# Step 1: 数据读取与预处理
file_path = '工作簿222.xlsx'
data = pd.read_excel(file_path)

# 筛选数据，选择2023-06-24到2023-06-30期间的数据
filtered_data = data[(data['销售日期'] >= '2023-06-24') & (data['销售日期'] <= '2023-06-30')]

# 计算单品的平均损耗率
grouped_data = filtered_data.groupby('单品名称').agg({'单品编码': 'first', '损耗率': 'mean'}).reset_index()

# 假设一些额外的约束条件，例如库存上限和最低利润率
max_inventory = 100  # 最大库存
min_profit_margin = 0.2  # 最低利润率，例如定价必须高于成本的20%
max_loss_rate = 0.5  # 限制损耗率影响最大为50%

# 调整定价策略：假设定价为成本的1.5倍到2倍，确保利润空间
grouped_data['成本'] = np.random.uniform(5, 15, size=len(grouped_data))
grouped_data['补货量'] = np.random.uniform(2.5, 20, size=len(grouped_data))
grouped_data['定价'] = grouped_data['成本'] * np.random.uniform(1.5, 2.0, size=len(grouped_data))


# Step 2: 调整目标函数，加入对损耗率影响的更高权重，并引入约束条件
def objective_function(supply_amount, pricing, cost, loss_rate, max_inventory, min_profit_margin, max_loss_rate):
    if supply_amount.sum() > max_inventory:
        print("库存上限未满足: 总补货量", supply_amount.sum())
        return None  # 改为返回None

    profit_margin = (pricing - cost) / cost
    if any(profit_margin < min_profit_margin):
        print("最低利润率未满足: 最低利润率为", profit_margin.min())
        return None  # 改为返回None

    loss_rate = np.minimum(loss_rate, max_loss_rate)

    revenue = supply_amount * (pricing - cost)
    loss = supply_amount * cost * loss_rate
    profit = revenue - loss

    if profit.sum() < 0:
        print("计算出的利润为负值: 总利润", profit.sum())

    return profit.sum()

def simulated_annealing(data, initial_temp=100, alpha=0.98, stopping_temp=1, max_iter=100, max_inventory=100,
                        min_profit_margin=0.2, max_loss_rate=0.5):
    current_solution = data.sample(n=29)
    current_temp = initial_temp
    best_solution = current_solution.copy()
    best_profit = objective_function(best_solution['补货量'], best_solution['定价'], best_solution['成本'],
                                     best_solution['损耗率'], max_inventory, min_profit_margin, max_loss_rate)

    while current_temp > stopping_temp:
        for i in range(max_iter):
            new_solution = current_solution.copy()
            perturbation_factor = np.random.uniform(0.9, 1.1)
            perturbed_index = np.random.choice(new_solution.index)

            # 添加一个判断逻辑，确保扰动不会直接导致违反库存上限
            new_supply_amount = new_solution['补货量'].copy()
            new_supply_amount[perturbed_index] *= perturbation_factor

            if new_supply_amount.sum() <= max_inventory:
                new_solution.at[perturbed_index, '补货量'] = new_supply_amount[perturbed_index]
            else:
                continue  # 跳过导致库存超限的解

            new_solution.at[perturbed_index, '定价'] *= perturbation_factor

            new_profit = objective_function(new_solution['补货量'], new_solution['定价'], new_solution['成本'],
                                            new_solution['损耗率'], max_inventory, min_profit_margin, max_loss_rate)

            if new_profit is None:
                print(f"新解无效，跳过：第{i}次迭代，温度 {current_temp:.2f}")
                continue

            if new_profit > best_profit:
                best_solution = new_solution.copy()
                best_profit = new_profit
                current_solution = new_solution.copy()
            else:
                if np.exp((new_profit - best_profit) / current_temp) > np.random.rand():
                    current_solution = new_solution.copy()

        current_temp *= alpha

    return best_solution, best_profit

# Step 4: 调用模拟退火算法求解最优解
best_solution, best_profit = simulated_annealing(grouped_data, max_inventory=max_inventory,
                                                 min_profit_margin=min_profit_margin, max_loss_rate=max_loss_rate)

# 输出每个单品的收益计算详情
best_solution['收益'] = best_solution.apply(
    lambda row: objective_function(pd.Series([row['补货量']]), pd.Series([row['定价']]), pd.Series([row['成本']]),
                                   pd.Series([row['损耗率']]), max_inventory, min_profit_margin, max_loss_rate), axis=1)

# 打印收益结果
print(best_solution[['单品名称', '补货量', '定价', '成本', '损耗率', '收益']])

# 打印总收益
print("最大收益为:", best_profit)

# Step 5: 输出结果，将最佳补货量和定价策略保存到Excel文件
output_path = os.path.expanduser('21最佳补货和定价策略.xlsx')
best_solution.to_excel(output_path, index=False)

print("最优单品补货量和定价策略已保存到:", output_path)