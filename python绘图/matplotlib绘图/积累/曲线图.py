import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 手动创建数据集
days = list(range(1, 101))  # 1到100天
temperature = [
    15, 16, 18, 19, 17, 16, 20, 22, 21, 19,
    18, 17, 23, 25, 24, 23, 22, 20, 19, 21,
    20, 22, 24, 26, 27, 28, 30, 29, 28, 27,
    26, 25, 23, 21, 22, 23, 24, 26, 27, 29,
    31, 32, 30, 29, 28, 26, 25, 24, 23, 22,
    21, 19, 20, 22, 23, 25, 24, 23, 22, 21,
    23, 24, 26, 28, 29, 30, 31, 32, 34, 35,
    36, 34, 33, 32, 30, 28, 27, 26, 24, 23,
    22, 20, 21, 23, 25, 26, 28, 30, 29, 28,
    27, 26, 25, 24, 23, 21, 20, 19, 18, 17
]
weather_type = [
    'sunny', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny', 'cloudy',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny',
    'cloudy', 'rainy', 'sunny', 'sunny', 'cloudy', 'cloudy', 'rainy', 'rainy', 'sunny', 'sunny'
]
location = [
    'north', 'north', 'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north',
    'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south',
    'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north',
    'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south',
    'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north',
    'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south',
    'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north',
    'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south',
    'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north',
    'north', 'south', 'south', 'north', 'north', 'south', 'south', 'north', 'north', 'south'
]
season = [
    'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring',
    'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring',
    'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer',
    'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer', 'summer',
    'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall',
    'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall', 'fall',
    'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter',
    'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter', 'winter',
    'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring',
    'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring', 'spring'
]

# 创建DataFrame
weather_data = pd.DataFrame({
    'day': days,
    'temperature': temperature,
    'weather_type': weather_type,
    'location': location,
    'season': season
})

# 设置图表大小
plt.figure(figsize=(10, 7))
sns.set_theme(style="whitegrid")

# 创建一个调色板
palette = sns.color_palette("rocket_r")

# 绘制折线图
sns.relplot(
    data=weather_data,
    x="day", y="temperature",
    hue="weather_type", size="location",
    palette=palette
)

# 添加标题和标签
plt.title('Temperature Over 100 Days by Weather Type and Location', fontsize=16, fontweight='bold')
plt.xlabel('Day', fontsize=14)
plt.ylabel('Temperature', fontsize=14)

plt.show()

