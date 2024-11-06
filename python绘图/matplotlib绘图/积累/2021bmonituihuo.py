import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
from scipy.optimize import dual_annealing

# 加载处理后的数据
data1_cleaned = pd.read_excel('处理后的附件1.xlsx')

# 将催化剂组合编号作为分类变量
data1_cleaned['催化剂组合编号'] = data1_cleaned['催化剂组合编号'].astype('category')

# 训练乙醇转化率的多元线性回归模型
model_etoh = smf.ols('Q("乙醇转化率(%)") ~ 温度 + Q("催化剂组合编号")', data=data1_cleaned).fit()

# 训练C4烯烃选择性的多元线性回归模型
model_c4 = smf.ols('Q("C4烯烃选择性(%)") ~ 温度 + Q("催化剂组合编号")', data=data1_cleaned).fit()

# 获取催化剂组合编号的类别
categories = data1_cleaned['催化剂组合编号'].cat.categories

# 定义目标函数：负的C4烯烃收率（因为我们用minimization来求解）
def objective_function(x):
    # x[0]为温度，x[1]为催化剂组合编号的索引
    temp = x[0]
    cat_combination = categories[int(x[1])]

    # 预测乙醇转化率和C4烯烃选择性
    pred_etoh = model_etoh.predict(pd.DataFrame({'温度': [temp], '催化剂组合编号': [cat_combination]}))
    pred_c4 = model_c4.predict(pd.DataFrame({'温度': [temp], '催化剂组合编号': [cat_combination]}))

    # 计算C4烯烃收率
    c4_yield = pred_etoh.iloc[0] * pred_c4.iloc[0]

    # 返回负的C4烯烃收率，因为我们要最大化它
    return -c4_yield

# 设置变量的边界
bounds = [(data1_cleaned['温度'].min(), data1_cleaned['温度'].max()),  # 温度的范围
          (0, len(categories) - 1)]  # 催化剂组合编号索引的范围

# 使用模拟退火算法优化
result = dual_annealing(objective_function, bounds)

# 提取最优解
optimal_temp = result.x[0]
optimal_combination_index = int(result.x[1])
optimal_combination = categories[optimal_combination_index]
max_c4_yield = -result.fun

# 输出结果
print(f"最优温度: {optimal_temp:.2f} °C")
print(f"最优催化剂组合: {optimal_combination}")
print(f"最大C4烯烃收率: {max_c4_yield:.4f}")