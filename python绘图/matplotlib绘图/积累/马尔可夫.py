import numpy as np

# a为一二关的实际天气 1代表晴朗 2代表高温 3代表沙暴
a = np.array([2, 2, 1, 3, 1, 2, 3, 1, 2, 2, 3, 2, 1, 2, 2, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 2, 2])

# 计算频率矩阵f
f = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        f[i, j] = np.sum((a[:-1] == i + 1) & (a[1:] == j + 1))

# 计算转移概率矩阵p
ni = np.sum(f, axis=1)
p = f / ni[:, np.newaxis]

# 初始天气：高温
firstp = np.array([0, 1, 0])

# 求解极限频率
for i in range(30):
    firstp = np.dot(firstp, np.linalg.matrix_power(p, i + 1))

jixianP = firstp
print("预测晴朗、高温、沙暴10天内出现次数")
fenbu = np.round(firstp * 10)

# 第3关10天内天气的模拟
disanguan_weather = np.random.choice([1, 2], 10, p=[3/8, 5/8])
disanguantianqi = []

for i in range(10):
    if disanguan_weather[i] == 1:
        disanguantianqi.append('晴朗')
    elif disanguan_weather[i] == 2:
        disanguantianqi.append('高温')

print(disanguantianqi)

# 第四关30天内天气的模拟
disiguan_weather = np.random.choice([1, 2, 3], 30, p=[0.3, 0.5, 0.2])
disiguantianqi4 = []

for i in range(30):
    if disiguan_weather[i] == 1:
        disiguantianqi4.append('晴朗')
    elif disiguan_weather[i] == 2:
        disiguantianqi4.append('高温')
    elif disiguan_weather[i] == 3:
        disiguantianqi4.append('沙暴')

print(disiguantianqi4)