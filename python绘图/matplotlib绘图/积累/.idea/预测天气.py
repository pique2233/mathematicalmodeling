import numpy as np

# 定义天气序列，1代表晴朗，2代表高温，3代表沙暴
a = np.array([2, 2, 1, 3, 1, 2, 3, 1, 2, 3, 2, 2, 1, 3, 2, 1, 1, 2, 2])

# 初始化转移矩阵
f = np.zeros((3, 3))

# 计算转移概率矩阵
for i in range(3):
    for j in range(3):
        f[i, j] = np.sum((a[:-1] == (i+1)) & (a[1:] == (j+1)))

ni = np.sum(f, axis=1)

# 转移概率矩阵
p = f / ni[:, None]

# 生成天气预测序列
firstp = np.array([0, 1, 0])
firstp = firstp @ np.linalg.matrix_power(p, 10)
print(f"预测晴朗、高温、沙暴10天内出现次数: {np.round(firstp * 10)}")

# 模拟生成随机天气序列
days = 10
# 确保概率总和为1
disanguan_weather = np.random.choice([1, 2, 3], size=days, p=[0.3, 0.5, 0.2])
disanguan_tianqi = ['晴朗' if w == 1 else '高温' if w == 2 else '沙暴' for w in disanguan_weather]

print(disanguan_tianqi)